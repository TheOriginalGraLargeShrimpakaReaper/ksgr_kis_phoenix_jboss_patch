import matplotlib.pyplot as plt
import numpy as np
import pip as pd
import os
import csv
import pandas as pd

def riskmatrix(risk, conf, matrix):
    # get the risk datas
    risk_conf = conf.get(risk)
    startpath = risk_conf.get('startpath')
    destination = risk_conf.get('destinatination')
    imagename = risk_conf.get('imagename')
    datafilename = risk_conf.get('datafilename')
    itemname = risk_conf.get('itemname')
    x_axis_title = risk_conf.get('x-axis-title')
    y_axis_title = risk_conf.get('y-axis-title')
    title = risk_conf.get('title')
    bubble_standard_size = int(risk_conf.get('bubble-standard-size'))

    if startpath == 'homedir':
        directory = os.path.join(os.getcwd(), destination)
    else:   # parentdir
        directory = os.path.join(os.path.dirname(os.getcwd()), destination)

    print(directory)

    # get the Datas as dirct
    data_path = os.path.join(directory, datafilename)
    image_path = os.path.join(directory, imagename)

    # load datas from csv into dict
    with open(data_path) as f:
        csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

    (_, *header), *data = csv_list
    datas = {}
    for row in data:
        key, *values = row
        datas[key] = {key: value for key, value in zip(header, values)}

    # fig_dir = os.path.join(os.path.dirname(os.getcwd()), 'src', 'source')
    fig = plt.figure()
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.xticks([])
    plt.yticks([])
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)

    #This example is for a 5 * 5 matrix
    nrows=5
    ncols=5
    axes = [fig.add_subplot(nrows, ncols, r * ncols + c + 1) for r in range(0, nrows) for c in range(0, ncols) ]

    # remove the x and y ticks
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0,5)
        ax.set_ylim(0,5)

    #Add background colors
    #This has been done manually for more fine-grained control
    #Run the loop below to identify the indice of the axes

    #Identify the index of the axes
    green = [10, 15, 16, 20 , 21] #Green boxes
    yellow = [0, 5, 6, 11, 17, 22, 23] #yellow boxes
    orange = [1 , 2, 7, 12, 13, 18, 19, 24] # orange boxes
    red = [3, 4, 8, 9, 14] #red boxes

    for _ in green:
        axes[_].set_facecolor('green')

    for _ in yellow:
        axes[_].set_facecolor('yellow')

    for _ in orange:
        axes[_].set_facecolor('orange')

    for _ in red:
        axes[_].set_facecolor('red')


    #Add labels to the Green boxes
    # axes[10].text(0.1,0.8, '4')
    # axes[15].text(0.1,0.8, '2')
    # axes[20].text(0.1,0.8, '1')
    # axes[16].text(0.1,0.8, '5')
    # axes[21].text(0.1,0.8, '3')

    #Add labels to the Yellow boxes
    # axes[0].text(0.1,0.8, '11')
    # axes[5].text(0.1,0.8, '7')
    # axes[6].text(0.1,0.8, '12')
    # axes[11].text(0.1,0.8, '8')
    # axes[17].text(0.1,0.8, '9')
    # axes[22].text(0.1,0.8, '6')
    # axes[23].text(0.1,0.8, '10')

    #Add lables to the Orange boxes
    # axes[1].text(0.1,0.8, '16')
    # axes[2].text(0.1,0.8, '20')
    # axes[7].text(0.1,0.8, '17')
    # axes[12].text(0.1,0.8, '13')
    # axes[13].text(0.1,0.8, '18')
    # axes[18].text(0.1,0.8, '14')
    # axes[19].text(0.1,0.8, '19')
    # axes[24].text(0.1,0.8, '15')

    #Add lables to the Red Boxes
    # axes[3].text(0.1,0.8, '23')
    # axes[8].text(0.1,0.8, '21')
    # axes[4].text(0.1,0.8, '25')
    # axes[9].text(0.1,0.8, '24')
    # axes[14].text(0.1,0.8, '22')

    # run throuh datas and generate axis datas
    dict_bubble_axis = dict()
    bubble_axis = list()
    for datasets in datas:
        # get the datas
        riskid = datas.get(datasets).get('risk-id')
        x_axis = int(datas.get(datasets).get('x-axis'))
        y_axis = int(datas.get(datasets).get('y-axis'))
        axis_point = matrix.get((x_axis, y_axis))
        x_axis_text = float(datas.get(datasets).get('x-axis-text'))
        y_axis_text = float(datas.get(datasets).get('y-axis-text'))
        x_axis_bubble = float(datas.get(datasets).get('x-axis-bubble'))
        y_axis_bubble = float(datas.get(datasets).get('y-axis-bubble'))
        bubble_axis.append(axis_point)

        # merge riks if two or more risks share the same axispoint
        if dict_bubble_axis.get(axis_point):
            risktag = dict_bubble_axis.get(axis_point).get('risk')
            risktag = risktag + '/' + riskid
            x_axis_text = x_axis_text + 0.25
            y_axis_text = y_axis_text - 0.5
            bubble_size = bubble_standard_size * 2
        else:
            risktag = itemname + riskid
            bubble_size = bubble_standard_size
        dict_axis_value = dict()

        dict_axis_value['risk'] = risktag
        dict_axis_value['x-axis-text'] = x_axis_text
        dict_axis_value['y-axis-text'] = y_axis_text
        dict_axis_value['x-axis-bubble'] = x_axis_bubble
        dict_axis_value['y-axis-bubble'] = y_axis_bubble
        dict_axis_value['size'] = bubble_size
        dict_bubble_axis[axis_point] = dict_axis_value

    # cleanup the list, remove duplicated entries
    bubble_axis = set(bubble_axis)

    # plot the bubbles and texts in the bubbles
    for axispoint in bubble_axis:
        axes[axispoint].scatter(dict_bubble_axis[axispoint]['x-axis-bubble'], dict_bubble_axis[axispoint]['y-axis-bubble'], dict_bubble_axis[axispoint]['size'], alpha=1)
        axes[axispoint].text(dict_bubble_axis[axispoint]['x-axis-text'], dict_bubble_axis[axispoint]['y-axis-text'], s=dict_bubble_axis[axispoint]['risk'], va='bottom', ha='center')

    # save the plot as image
    plt.savefig(image_path)

"""
Config File:
    1.  Name
    2.  Startpoint Directory
    3.  Destination Dir
    4.  Alternate Path
    5.  Data File Name
Data File:
    1.  Spalte:  Nummer
    2.  x-achse
    3.  x-achse
"""

"""
    Matrix
    This Matrix translate the x/y axis from a given risk matrix csv to the axispoint.
    
    The key of each axispoint is an integer tupel (x, y)
    So, you can access the axis point this way:
    <axispoint> = matrix.get((<x_axis>, <y_axis>))
"""
matrix = {
     # first column
     (1, 1):20,
     (1, 2):15,
     (1, 3):10,
     (1, 4):5,
     (1, 5):0,
     # second column
     (2, 1):21,
     (2, 2):16,
     (2, 3):11,
     (2, 4):6,
     (2, 5):1,
     # third column
     (3, 1): 22,
     (3, 2): 17,
     (3, 3): 12,
     (3, 4): 7,
     (3, 5): 2,
     # fourth column
     (4, 1): 23,
     (4, 2): 18,
     (4, 3): 13,
     (4, 4): 8,
     (4, 5): 3,
     # fifth column
     (5, 1): 24,
     (5, 2): 19,
     (5, 3): 14,
     (5, 4): 9,
     (5, 5): 4
}

# load the configuration file
riskmatrix_conf_filename = 'conf.csv'
riskmatrix_conf_dir = 'src/source/configuration/'
conf_riskmatrix_path = os.path.join(os.path.dirname(os.getcwd()), riskmatrix_conf_dir)
conf_csv_path = os.path.join(conf_riskmatrix_path, riskmatrix_conf_filename)
with open(conf_csv_path) as f:
    csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

(_, *header), *data = csv_list
conf = {}
for row in data:
    key, *values = row
    conf[key] = {key: value for key, value in zip(header, values)}

for risks in conf:
    riskmatrix(risks, conf, matrix)
# data = pd.read_csv('/home/itgramic/LaTex/riskmatrix/src/source/riskmatrixproblem.csv', header=None, dtype={0: str}).set_index(0).squeeze().to_dict()
