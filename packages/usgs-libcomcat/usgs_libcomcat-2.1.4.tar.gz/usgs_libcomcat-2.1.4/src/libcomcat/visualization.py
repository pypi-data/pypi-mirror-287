from datetime import timedelta
import numpy as np
import pandas as pd
import pathlib
import math
import json
import matplotlib.pyplot as plt
from esi_utils_rupture.quad_rupture import QuadRupture
from esi_utils_rupture.origin import Origin
from obspy.imaging.beachball import beach
from esi_utils_colors.cpalette import ColorPalette
from io import StringIO
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

PRODUCT_COLORS = {"finite-fault": "#C5CAF5", 
                  "ground-failure": "#A2F5EF", 
                  "losspager": "#F6D5E4", 
                  "moment-tensor": "#C9DCF5",
                  "origin": "#CEF3B4",
                  "shakemap": "#FFEFD5",
                  "dyfi": "#44B4F4",
                  "oaf": "#BBFF99",
                  "phase-data": "#F5B69C",
                  "default": "#72DCB7",
                  "focal-mechanism": "#EC7063"}

def create_timeline(max_time, dataframe, event_details):
    
    if max_time > 5760:
        max_time = 5760

    else:
        max_time = max_time

    shortened_history = dataframe.loc[(dataframe["Product"] != 'dyfi') & (dataframe["Product"] != 'phase-data') & (dataframe["Elapsed (min)"] < max_time) & (dataframe["Elapsed (min)"] >= 0) & (dataframe["Product"] != 'oaf')] # not including dyfi or oaf products in timeline, not including anything done 4 days later

    max_time = float(shortened_history.iloc[-1]["Elapsed (min)"])

    dyfi_frame = dataframe[dataframe["Product"] == 'dyfi']
    dyfi_frame = dyfi_frame.loc[(dyfi_frame ['Description'].str.split('|').str[1].str.split('# ').str[1] != '0') & (dyfi_frame["Elapsed (min)"] < max_time) & (dyfi_frame["Elapsed (min)"] >= 0)]

    oaf_frame = dataframe[dataframe["Product"] == 'oaf']
    oaf_frame = oaf_frame.loc[(oaf_frame["Elapsed (min)"] < max_time) & (oaf_frame["Elapsed (min)"] >= 0)]

    if shortened_history.empty:
        print("No data available to create a timeline.")
        return

    # keeps track of the total instances and the instances in each time block
    # time blocks were determined by observing data from different earthquakes
    #  and determining time blocks that commonly had earthquakes, whether that
    #  be individual hours or groups of hours
    total = 0
    hr_1 = 0
    hr_2_3 = 0
    hr_4 = 0
    hr_4_7 = 0
    hr_7_10 = 0
    hr_10_20 = 0
    hr_20_24 = 0
    hr_24 = 0

    # calculates how many instances are present in each time block
    for idx, row in shortened_history.iterrows():
        if row["Elapsed (min)"] <= 60:
            hr_1 += 1
        elif row["Elapsed (min)"] <= 180:
            hr_2_3 += 1
        elif row["Elapsed (min)"] <= 240:
            hr_4 += 1
        elif row["Elapsed (min)"] <= 420:
            hr_4_7 += 1
        elif row["Elapsed (min)"] <= 600:
            hr_7_10 += 1
        elif row["Elapsed (min)"] <= 1200:
            hr_10_20 += 1
        elif row["Elapsed (min)"] <= 1440:
            hr_20_24 += 1
        else:
            hr_24 += 1
        total += 1

    # calculates how much of the timeline should be dedicated to each time block
    DEFAULT_1HR_SPACE = hr_1 / total
    DEFAULT_2_3_SPACE = hr_2_3 / total
    DEFAULT_4HR_SPACE = hr_4 / total
    DEFAULT_4_7_SPACE = hr_4_7 / total
    DEFAULT_7_10_SPACE = hr_7_10 / total
    DEFAULT_10_20_SPACE = hr_10_20 / total
    DEFAULT_20_24_SPACE = hr_20_24 / total
    DEFAULT_24_SPACE = hr_24 / total

    figure, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,10))
    plt.sca(ax)
    # draws an arrow representing the timeline
    arrow_middle = 0.5
    arrow_width = 0.01
    arrow_length = np.ceil(shortened_history.iloc[-1]["Elapsed (min)"]/60)
    head_length = arrow_length * 0.05
    head_width = arrow_width * 2
    plt.arrow(0, arrow_middle, arrow_length, 0, head_width = head_width, width = arrow_width, head_length=head_length, facecolor=(200/255,200/255,200/255))

    # times that will show up on the timeline if their time block is given space
    notable_times = [(0,"Origin"),(10,"10 min"), (20,"20 min"), (30,"30 min"),
                    (60,"1 h"), (120,"2 h"), (180,"3 h"), (240, "4 h"), 
                    (420, '7 h'), (600, '10 h'), (1200, '20 h'), (1440,"1 d"),
                    (2880,"2 d"), (4320,"3 d"), (5760, "4 d")]

    i = 0
    # start and end keep track of which blocks of time are skipped
    start = -1      
    end = -1

    # plots the notable times on the timeline, along with blocks describing time periods skipped
    while i < len(notable_times) and notable_times[i][0] < shortened_history.iloc[-1]["Elapsed (min)"]:

        plot = -1

        if notable_times[i][0] <= 60:       
            # if time is less than or equal to 1 hr
            if DEFAULT_1HR_SPACE > 0:       
                # if the 1hr block has space on timeline
                plot = notable_times[i][0] / 60 * DEFAULT_1HR_SPACE * arrow_length  # determine the position of the textbox for the time
            else:           
                # if no space is dedicated for 1hr start tracking how many time 
                # blocks are skipped
                start = 0
                end = 1
        elif notable_times[i][0] < 180:     
            # if time is less than 3 hr
            if DEFAULT_2_3_SPACE > 0:       
                # if the 1-3hr block has space on timeline
                plot = (notable_times[i][0] - 60) / 120 * DEFAULT_2_3_SPACE * arrow_length + DEFAULT_1HR_SPACE * arrow_length   # determine the position of the textbox for the time

                if start == 0:      
                    # if the 1-3 hr block is on the timeline, but the one 
                    # before it is not, create a skipped indication and reset 
                    # the start value
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text((DEFAULT_1HR_SPACE - 0.005) * arrow_length, arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                    start = -1
            else:       
                # if no space is dedicated to the 1-3hr block
                if start != 0:      
                    # if the previous block was not skipped set the start and 
                    # end with the start and end values of the 1-3hr block
                    start = 1
                    end = 3
                else:               
                    # if the previous block was skipped set only the end value
                    end = 3

                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text((DEFAULT_1HR_SPACE - 0.005)* arrow_length, arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] < 240:
            if DEFAULT_4HR_SPACE > 0:
                plot = (notable_times[i][0] - 180) / 60 * DEFAULT_4HR_SPACE * arrow_length + (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE) * arrow_length

                if start == 0 or start == 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text((DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE - 0.005) * arrow_length, arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                    start = -1
            else:
                if start != 0 and start != 1:
                    start = 3
                    end = 4
                else:
                    end = 4

                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text((DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE - 0.005) * arrow_length, arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] < 420:
            if DEFAULT_4_7_SPACE > 0.0:
                plot = arrow_length * (DEFAULT_4_7_SPACE) * (notable_times[i][0] - 240) / 180 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE)
            
                if start == 0 or start == 1 or start == 3:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                    start = -1
            else:
                if start != 0 and start != 1 and start !=3:
                    start = 4
                    end = 7
                else:
                    end = 7

                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] < 600:
            if DEFAULT_7_10_SPACE > 0.0:
                plot = arrow_length * (DEFAULT_7_10_SPACE) * (notable_times[i][0] - 420) / 180 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE)

                if start == 0 or start == 1 or start == 3 or start == 4:
                        plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                        plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                        start = -1
            else:
                if start != 0 and start != 1 and start != 3 and start != 4:
                    start = 7
                    end = 10
                else:
                    end = 10

                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] < 1200:
            if DEFAULT_10_20_SPACE > 0.0:
                plot = arrow_length * (DEFAULT_10_20_SPACE) * (notable_times[i][0] - 600) / 600 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE)

                if start == 0 or start == 1 or start == 3 or start == 4 or start == 7:
                        plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                        plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                        start = -1
            else:
                if start != 0 and start != 1 and start != 3 and start != 4 and start != 7:
                    start = 10
                    end = 20
                else:
                    end = 20
                
                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] < 1440:
            if DEFAULT_20_24_SPACE > 0.0:
                plot = arrow_length * (DEFAULT_20_24_SPACE) * (notable_times[i][0] - 1200) / 240 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE)

                if start == 0 or start == 1 or start == 3 or start == 4 or start == 7 or start == 10:
                        plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                        plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

                        start = -1
            else:
                if start != 0 and start != 1 and start != 3 and start != 4 and start != 7 and start != 10:
                    start = 20
                    end = 24
                else:
                    end = 24

                if i == len(notable_times) - 1:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE - 0.005), arrow_middle - arrow_width, arrow_middle + 1.5 * arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))
        elif notable_times[i][0] >= 1440:
            if DEFAULT_24_SPACE > 0.0:
                plot = arrow_length * (DEFAULT_24_SPACE) * np.log((notable_times[i][0] - 1440) / 60 / arrow_length + 1) + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE + DEFAULT_20_24_SPACE)

                if i == len(notable_times) - 1 or start == 0 or start == 1 or start == 3 or start == 4 or start == 7 or start == 10 or start == 20:
                    plt.vlines(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE + DEFAULT_20_24_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, arrow_middle + arrow_width / 2, colors='red')

                    plt.text(arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE + DEFAULT_20_24_SPACE - 0.005), arrow_middle - 1.5 * arrow_width, f'{start}-{end}h', rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white', edgecolor="red"))

        if plot != -1:
            plt.text(plot, arrow_middle, notable_times[i][1], rotation=0, rotation_mode="anchor", fontsize=7, bbox=dict(facecolor='white'))

            plt.vlines(plot, arrow_middle - arrow_width, arrow_middle + arrow_width, colors='black')
        i+=1

    shortened_history = pd.concat([shortened_history, dyfi_frame, oaf_frame])

    plt.vlines(arrow_length, arrow_middle + arrow_width, arrow_middle + 20 * arrow_width, colors=(200/255,200/255,200/255))

    nresp = shortened_history[shortened_history["Product"]=='dyfi'].tail(1)["Description"].values[0].split("|")[1].split("# ")[1]
    order = max(math.floor(np.log10(int(nresp))), 1)
    max_dyfi = math.ceil(int(nresp)/(10 ** order)) * 10 ** order

    for i in range(1,11):
        tick_dyfi = int(max_dyfi * 0.1 * i)
        plt.text(arrow_length, arrow_middle + arrow_width * 20 * 0.1 * i, tick_dyfi, fontsize=7, bbox=dict(facecolor='white', edgecolor=(150/255,150/255,150/255)), color=(150/255,150/255,150/255))

    plt.text(arrow_length, arrow_middle + arrow_width * 20 * 1.1, "DYFI \n Responses", fontsize=7, bbox=dict(facecolor='white', edgecolor=(150/255,150/255,150/255)), color=(150/255,150/255,150/255))

    top = 1             # top controls whether an instance is on the top or bottom of the timeline
    top_count = 0       # top_count and other_count determine which level an instance in on on the top or bottom of the timeline
    other_count = 0

    dyfi_x = []
    dyfi_y = []
    dyfi = False

    oaf = False

    # plots the instances
    for idx, row in shortened_history.iterrows():
        ptype = row["Product"]
        elapsed_min = row["Elapsed (min)"]
        elapsed = elapsed_min/60.0
        psource = row["Product Source"]

        product_row = row["Description"].split("|")

        if ptype == "ground-failure":
            landslide = product_row[-1].split("# ")[1]
            liquefaction = product_row[-2].split("# ")[1]
            product_statement = f"\n"

        elif ptype == "dyfi":
            product_statement = ""

        else:
            product_summary = product_row[0].split("# ")[1]

            if ptype == "origin":
                product_summary = f"{product_row[-4].split("# ")[1]} {product_summary}"
                product_statement = f""
            elif ptype == "shakemap":
                product_statement = f""
            elif ptype == "losspager":
                product_statement = f""
            elif ptype == "finite-fault":
                product_statement = f"\n"
            elif ptype == "moment-tensor":
                beachball_stats = [int(product_row[-3].split("# ")[1]), int(product_row[-2].split("# ")[1]), int(product_row[-1].split("# ")[1])]

                magnitude = product_row[1].split("# ")[1]

                product_statement = f"{product_summary}  {magnitude} \n"

        # determines the statement and horizontal location of text boxes
        if elapsed_min <= 60:
            elapsed = elapsed * DEFAULT_1HR_SPACE * arrow_length
            pstring = f"{(elapsed_min):.1f} min: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 180:
            elapsed = (elapsed_min - 60) / 120 * arrow_length * DEFAULT_2_3_SPACE + DEFAULT_1HR_SPACE * arrow_length
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 240:
            elapsed = (elapsed_min - 180) / 60 * arrow_length * DEFAULT_4HR_SPACE + (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE) * arrow_length
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 420:
            elapsed = arrow_length * (DEFAULT_4_7_SPACE) * (elapsed_min - 240) / 180 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE)
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 600:
            elapsed = arrow_length * (DEFAULT_7_10_SPACE) * (elapsed_min - 420) / 180 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE)
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 1200:
            elapsed = arrow_length * (DEFAULT_10_20_SPACE) * (elapsed_min - 600) / 600 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE)
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        elif elapsed_min < 1440:
            elapsed = arrow_length * (DEFAULT_20_24_SPACE) * (elapsed_min - 1200) / 240 + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE)
            pstring = f"{(elapsed_min / 60):.1f} hrs: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"
        else:
            elapsed = arrow_length * (DEFAULT_24_SPACE) * np.log((elapsed_min - 1440) / 60 / arrow_length + 1) + arrow_length * (DEFAULT_1HR_SPACE + DEFAULT_2_3_SPACE + DEFAULT_4HR_SPACE + DEFAULT_4_7_SPACE + DEFAULT_7_10_SPACE + DEFAULT_10_20_SPACE + DEFAULT_20_24_SPACE)
            pstring = f"{(elapsed_min / 1440):.1f} d: {psource.upper()} \n {ptype.capitalize()} \n {product_statement}"

        if ptype != "dyfi" and ptype != "oaf":

            if top:
                if top_count % 4 == 0:
                    ytext = arrow_middle+(arrow_width * 5)
                elif top_count % 4 == 1:
                    ytext = arrow_middle+(arrow_width * 10)
                elif top_count % 4 == 2:
                    ytext = arrow_middle+(arrow_width * 15)
                else:
                    ytext = arrow_middle+(arrow_width * 20)
                fontsize = 10
                if (ptype == "moment-tensor" or ptype == "ground-failure" or ptype == "finite-fault"):
                    fontsize = 9
                top = 0
                top_count+=1
                plt.vlines(elapsed, arrow_middle+arrow_width/2, ytext, colors="black")
            else:
                if other_count % 4 == 0:
                    ytext = arrow_middle-(arrow_width * 6)
                elif other_count % 4 == 1:
                    ytext = arrow_middle-(arrow_width * 11)
                elif other_count % 4 == 2:
                    ytext = arrow_middle-(arrow_width * 16)
                else:
                    ytext = arrow_middle-(arrow_width * 21)
                fontsize = 10
                if (ptype == "moment-tensor" or ptype == "ground-failure" or ptype == "finite-fault"):
                    fontsize = 9
                top = 1
                other_count+=1
                plt.vlines(elapsed, ytext, arrow_middle-arrow_width/2, colors="black")
                
            plt.text(elapsed, ytext, pstring, rotation=0, rotation_mode="anchor", fontsize=fontsize, bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS[ptype]), color="black")

            if ptype == "moment-tensor":
                bball = beach(beachball_stats, xy = (elapsed + arrow_length * 0.06, ytext + 0.5 * arrow_width), size = 25, width = 25, axes=ax, facecolor="#61BFFA", linewidth=1)

                ax.add_collection(bball)

            elif ptype == "losspager":
                pager_colors = {"red": "#FF0000", "orange": "#FF9900", "yellow": "#FFFF00", "green": "#00B04F"}
                plt.text(elapsed + arrow_length * 0.005, ytext - 0.1 * arrow_width, product_summary.upper(), rotation=0, rotation_mode="anchor", fontsize=9, bbox=dict(facecolor=pager_colors[product_summary.lower()], pad=1))

            elif ptype == "finite-fault":

                origin = {}

                origin["id"] = event_details.id
                origin["time"] = event_details.time
                origin["locstring"] = event_details.location
                origin["lat"] = event_details.latitude
                origin["lon"] = event_details.longitude
                origin["depth"] = event_details.depth
                origin["mag"] = event_details.magnitude
                origin["alert"] = event_details.alert
                origin["netid"] = event_details['net']
                origin["network"] = ""


                origin = Origin(origin)

                ffault = event_details.getProducts("finite-fault")[0] # get the most recent finite fault product

                contents, _ = ffault.getContentBytes("shakemap_polygon.txt")

                fobj = StringIO(contents.decode("utf8"))

                lines = fobj.readlines()[3:-1]

                data = []
                for line in lines:
                    row = line.strip().split()
                    data.append(row)

                quad = QuadRupture.fromVertices([data[0][0]], [data[0][1]], [data[0][2]], [data[1][0]], [data[1][1]], [data[1][2]], [data[2][0]], [data[2][1]], [data[2][2]], [data[3][0]], [data[3][1]], [data[3][2]], origin)

                length = round(quad.getLength(),2)
                width = round(quad.getWidth(),2)

                text = f"L: {length} \nW: {width}"

                plt.text(elapsed + arrow_length * 0.005, ytext - 0.1 * arrow_width, text, rotation=0, rotation_mode="anchor", fontsize=8.5, bbox=dict(facecolor="#E3E8FC", pad=1))
                
            elif ptype == "shakemap":
                roman_numerals = {0: "0", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
                palette = ColorPalette.fromPreset("mmi")
                color = palette.getDataColor(float(product_summary), color_format="hex")
                text_sm = roman_numerals[int(round(float(product_summary)))]
                plt.text(elapsed + arrow_length * 0.005, ytext - 0.1 * arrow_width, text_sm, rotation=0, rotation_mode="anchor", fontsize=9, bbox=dict(facecolor=color, pad=1))

            elif ptype == "origin":
                plt.text(elapsed + arrow_length * 0.005, ytext - 0.1 * arrow_width, product_summary, rotation=0, rotation_mode="anchor", fontsize=9, bbox=dict(facecolor="#8AFF8A", pad=1))

            elif ptype == "ground-failure":
                landslide_imgs = {"red": "gf-landslide-red.png", "green": "gf-landslide-green.png", "yellow": "gf-landslide-yellow.png", "orange": "gf-landslide-orange.png"}
                liquefaction_imgs = {"red": "gf-liquefaction-red.png", "green": "gf-liquefaction-green.png", "yellow": "gf-liquefaction-yellow.png", "orange": "gf-liquefaction-orange.png"}
                
                landslide_path = pathlib.Path(__file__).parent / "data" / str(landslide_imgs[landslide])
                landslide_img = plt.imread(landslide_path)
                imagebox = OffsetImage(landslide_img, zoom = 0.05)
                ab = AnnotationBbox(imagebox, (elapsed + 0.02 * arrow_length, ytext + 0.45 * arrow_width), frameon = False)
                ax.add_artist(ab)

                liquefaction_path = pathlib.Path(__file__).parent / "data" / str(liquefaction_imgs[liquefaction])
                liquefaction_img = plt.imread(liquefaction_path)
                imagebox = OffsetImage(liquefaction_img, zoom = 0.05)
                ab = AnnotationBbox(imagebox, (elapsed + 0.055 * arrow_length, ytext + 0.45 * arrow_width), frameon = False)
                ax.add_artist(ab)
        elif ptype == "dyfi":
            if int(row["Description"].split("|")[1].split("# ")[1]) != 0:
                dyfi_x.append(elapsed)
                dyfi_y.append(arrow_middle + arrow_width * 20 * (int(row["Description"].split("|")[1].split("# ")[1])/int(nresp)))

            dyfi = True

        elif ptype == "oaf":
            oaf = event_details.getProducts("oaf")[0]
            data, _ = oaf.getContentBytes("forecast.json")
            fobj = StringIO(data.decode("utf8"))
            jdict = json.load(fobj)

            percentages = ["% Week 1"]
            occurences = ["Occurrences"]

            for forecast in jdict["forecast"]:
                if forecast["label"] == "1 Week":
                    for i in range(0,5):
                        percentage = f"{int(float(forecast['bins'][i]['probability'])*100)}%"
                        percentages.append(percentage)

            for i in range(0,5):
                occurences.append(jdict['observations'][i]['count'])

            oaf = True


    if dyfi:
        ax.scatter(dyfi_x, dyfi_y, color=PRODUCT_COLORS["dyfi"], zorder=-1, alpha = 0.3)
        ax.plot(dyfi_x, dyfi_y, color=PRODUCT_COLORS["dyfi"], zorder=-1, linewidth=3, alpha = 0.3)
    else:
        print("No DYFI responses to plot.")

    if oaf:
        table_text = [["Magnitude", "3+", "4+", "5+", "6+", "7+"], percentages, occurences]

        table = ax.table(cellText=table_text, loc="lower right", fontsize=8, bbox=[0.85, -0.15, 0.15, 0.1], colWidths=[0.05, 0.02, 0.02, 0.02, 0.02, 0.02], cellLoc="center", cellColours=[[PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"]], [PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"]], [PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"],PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"], PRODUCT_COLORS["oaf"]]])

        ax.text(0.85, -0.045, "Aftershock Forecast", fontsize=8, transform=ax.transAxes)

    else:
        print("No available OAF data.")

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.text(0.0005, 1.097, " Origin               ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["origin"]), color="black", transform=ax.transAxes)
    plt.text(0.0005, 1.073, " Losspager         ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["losspager"]), color="black", transform=ax.transAxes)
    plt.text(0.0005, 1.047, " Shakemap        ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["shakemap"]), color="black", transform=ax.transAxes)
    plt.text(0.0005, 1.023, " Finite-fault        ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["finite-fault"]), color="black", transform=ax.transAxes)
    plt.text(0.0005, 0.997, " Ground-failure  ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["ground-failure"]), color="black", transform=ax.transAxes)
    plt.text(0.0005, 0.973, " Moment-tensor ", fontsize=8, ha='left', va='top', bbox=dict(edgecolor='black', facecolor=PRODUCT_COLORS["moment-tensor"]), color="black", transform=ax.transAxes)
    plt.text(0, 1.1, "                     \n\n\n\n\n\n", ha='left', va='top', fontsize=10, bbox=dict(facecolor="none", linewidth=4), transform=ax.transAxes)

    ax.set_title(f'Event ID: {event_details.id}     Location: {event_details.location}     Day: {str(event_details.time).split()[0]}     Magnitude: {event_details.magnitude}', y=1.05)

    return figure