import os
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import shapefile as shp
from django.conf import settings

matplotlib.use('Agg')  # watch this line
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10, 6))

shp_path = "./maps/District.shp"
sf = shp.Reader(shp_path)


def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords'
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df


def plot_shape(id, s=None):
    """ PLOTS A SINGLE SHAPE """
    plt.figure()
    # ax = plt.axes()
    # ax.set_aspect('equal')
    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    plt.plot(x_lon, y_lat)
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=15)
    # use bbox (bounding box) to set plot limits
    plt.xlim(shape_ex.bbox[0], shape_ex.bbox[2])
    return x0, y0


def plot_map(sf, x_lim=None, y_lim=None, figsize=(11, 9)):
    '''
    Plot map with lim coordinates
    '''
    plt.figure(figsize=figsize)
    id = 0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')

        if (x_lim is None) & (y_lim is None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id += 1

    if (x_lim is not None) & (y_lim is not None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)


def plot_map2(id, sf, x_lim=None, y_lim=None, figsize=(11, 9)):
    '''
    Plot map with lim coordinates
    '''

    plt.figure(figsize=figsize)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')

    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    plt.plot(x_lon, y_lat, 'r', linewidth=3)

    if (x_lim is not None) & (y_lim is not None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)


def plot_map_fill(id, sf, x_lim=None,
                  y_lim=None,
                  figsize=(11, 9),
                  color='r'):
    '''
    Plot map with lim coordinates
    '''

    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    ax.fill(x_lon, y_lat, color)

    if (x_lim is not None) & (y_lim is not None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)


# plot_map_fill(0, sf, color='g')


def plot_map_fill_multiples_ids(title, comuna, sf, code, comunas,
                                x_lim=None,
                                y_lim=None,
                                figsize=(11, 9),
                                color='c', show_title=True, add_name=True):
    '''
    Plot map with lim coordinates
    '''

    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    if show_title:
        fig.suptitle(title, fontsize=16)
    ax.grid(False)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')
    com_id = 0
    for id in comuna:
        shape_ex = sf.shape(id)
        x_lon = np.zeros((len(shape_ex.points), 1))
        y_lat = np.zeros((len(shape_ex.points), 1))
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        ax.fill(x_lon, y_lat, color)
        if add_name is not False:
            x0 = np.mean(x_lon)
            y0 = np.mean(y_lat)
            plt.text(x0, y0, comunas[com_id], fontsize=10)
            com_id += 1

    if (x_lim is not None) & (y_lim is not None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)

    image_path = "maps/%s.png" % code
    fig.savefig("%s/%s" % (settings.MEDIA_ROOT, image_path))
    plt.close()
    return image_path


# comuna_id = [0, 1, 2, 3, 4, 5, 6, 20, 25]
# plot_map_fill_multiples_ids("Multiple Shapes",
#                             comuna_id, sf, color='g')


def plot_comunas_2(sf, title, comunas, color, code, show_title, add_name=True):
    '''
    Plot map with selected comunes, using specific color
    '''

    df = read_shapefile(sf)
    comuna_id = []
    for i in comunas:
        d_id = df[df.District == i].index[0]
        comuna_id.append(d_id)
#     print(comuna_id)
    return plot_map_fill_multiples_ids(
        title, comuna_id, sf, code, comunas, x_lim=None, y_lim=None, figsize=(11, 9), color=color, show_title=show_title, add_name=add_name)


# districts = ['Musanze', 'Gicumbi', 'Burera']
# plot_comunas_2(sf, 'Favorable districts for Acacia', districts, 'c')


def calc_color(data, color=None):
    if color == 1:
        color_sq = ['#dadaebFF', '#bcbddcF0', '#9e9ac8F0',
                    '#807dbaF0', '#6a51a3F0', '#54278fF0']
        colors = 'Purples'
    elif color == 2:
        color_sq = ['#c7e9b4', '#7fcdbb', '#41b6c4',
                    '#1d91c0', '#225ea8', '#253494']
        colors = 'YlGnBu'
    elif color == 3:
        color_sq = ['#f7f7f7', '#d9d9d9', '#bdbdbd',
                    '#969696', '#636363', '#252525']
        colors = 'Greys'
    elif color == 9:
        color_sq = ['#ff0000', '#ff0000', '#ff0000',
                    '#ff0000', '#ff0000', '#ff0000']
    else:
        color_sq = ['#ffffd4', '#fee391', '#fec44f',
                    '#fe9929', '#d95f0e', '#993404']
        colors = 'YlOrBr'
    new_data, bins = pd.qcut(data, 6, retbins=True,
                             labels=list(range(6)))
    color_ton = []
    for val in new_data:
        color_ton.append(color_sq[val])
    return color_ton, bins


def plot_map_fill_multiples_ids_tone(sf, title, comuna,
                                     print_id, color_ton,
                                     bins, comunas,
                                     x_lim=None,
                                     y_lim=None,
                                     figsize=(11, 9)):
    '''
    Plot map with lim coordinates
    '''

    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(title, fontsize=16)
    ax.grid(False)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    for id in comuna:
        shape_ex = sf.shape(id)
        x_lon = np.zeros((len(shape_ex.points), 1))
        y_lat = np.zeros((len(shape_ex.points), 1))
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        ax.fill(x_lon, y_lat, color_ton[comuna.index(id)])
        if print_id is not False:
            x0 = np.mean(x_lon)
            y0 = np.mean(y_lat)
            plt.text(x0, y0, comunas[id], fontsize=10)
    if (x_lim is not None) & (y_lim is not None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)
    # name = random.randint(1450, 29849)
    # fig.savefig("./media/maps/%s.png" % name)
    # # print(img.path)
    # sp = Species()
    # sp.image = 'maps/%s.png' % name
    # sp.save()


def plot_comunas_data(sf, title, comunas, data=None,
                      color=None, print_id=False):
    '''
    Plot map with selected comunes, using specific color
    '''

    color_ton, bins = calc_color(data, color)
    df = read_shapefile(sf)
    comuna_id = []
    for i in comunas:
        d_id = df[df.District == i].index[0]
        comuna_id.append(d_id)
    # print(comuna)
    plot_map_fill_multiples_ids_tone(sf, title, comuna_id,
                                     print_id,
                                     color_ton,
                                     bins, comunas,
                                     x_lim=None,
                                     y_lim=None,
                                     figsize=(11, 9))


# south = ['Rulindo', 'Burera', 'Gasabo', 'Nyagatare', 'Bugesera']
# data = [100, 2000, 300, 400000, 500]
# print_id = True  # The shape id will be printed
# color_pallete = 1  # 'Purples'
# plot_comunas_data(sf, 'South', south, data, color_pallete, print_id)
