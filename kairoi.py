# -*- coding: utf-8 -*-
# Calendar Builder
# Generates a printable half-page calendar that I can use in my planner

# Kairos (Ancient Greek: καιρός) is an Ancient Greek word meaning the right,
# critical, or opportune moment.[1] The ancient Greeks had two words for time:
# chronos (χρόνος) and kairos. The former refers to chronological or sequential
# time, while the latter signifies a proper or opportune time for action. While
# chronos is quantitative, kairos has a qualitative, permanent nature.[2] Kairos
# also means weather in Modern Greek. The plural, καιροί (kairoi (Ancient and
# Modern Greek)) means the times. Kairos is a term, idea, and practice that has
# been applied in several fields including classical rhetoric, modern rhetoric,
# digital media, Christian theology, and science.

import calendar
import matplotlib.pyplot as plt


# TODO: Read in the date files

# TODO: Generate the calendar

# TODO: Set these up as settings that get passed around to the functions
# Set up some constants
# 11" x 8.5" paper size is 791 x 612 points
page_width = 791
page_height = 612

# gutters
gutter_width = 36

# calendar size
day_width = (page_width/4.0 - 1.5*gutter_width)/7.0
day_height = day_width

# space between calendars
calendar_padding = gutter_width

def generatePageFigure():
    '''Set up the page for printing'''

    # Generate the figure
    fig = plt.figure()
    fig.set_size_inches(11, 8.5)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    # DEBUG: plot some guides
    # centerfold
    plt.plot([page_width/2.0, page_width/2.0], [0, -page_height], '--k', linewidth=0.5)

    # gutters
    if (0):
        plt.plot([0, page_width], [-gutter_width, -gutter_width], 'c', linewidth=0.5)
        plt.plot([0, page_width], [-page_height + gutter_width, -page_height + gutter_width], 'c', linewidth=0.5)
        plt.plot([gutter_width, gutter_width], [0, -page_height], 'c', linewidth=0.5)
        plt.plot([page_width-gutter_width, page_width-gutter_width], [0, -page_height], 'c', linewidth=0.5)

        # centerfold of half-page
        plt.plot([page_width/2.0 + page_width/4.0, page_width/2.0 + page_width/4.0], [0, -page_height], '--b', linewidth=0.5)
        plt.plot([page_width/2.0 + page_width/4.0 - gutter_width/2.0, page_width/2.0 + page_width/4.0 - gutter_width/2.0], [0, -page_height], 'c', linewidth=0.5)
        plt.plot([page_width/2.0 + page_width/4.0 + gutter_width/2.0, page_width/2.0 + page_width/4.0 + gutter_width/2.0], [0, -page_height], 'c', linewidth=0.5)

        # half-page gutter
        plt.plot([page_width/2.0 - gutter_width, page_width/2.0 - gutter_width], [0, -page_height], 'c', linewidth=0.5)
        plt.plot([page_width/2.0 + gutter_width, page_width/2.0 + gutter_width], [0, -page_height], 'c', linewidth=0.5)

    plt.ylim(-page_height, 0)
    plt.xlim(0, page_width)

    return fig

def plotMonth(year, month, fig, xy, flagFull=False):
    '''Plot a month.'''

    # Create the calendar object
    c = calendar.monthcalendar(year, month)


    # TODO: I need a GOOD font with good unicode support
    # TODO: Replace payday number with '$'
    # TODO: Replace birthday number with '🎂' or '🕯 '
    # TODO: Change font color for weekend days (and off-fridays)
    # TODO: Highlight sprint start dates (and increment start dates)
    color_workday = '#000000'
    color_weekend = '#777755'
    color_weekend = '#476180'
    color_weekend = '#6790C2'


    # Draw the months
    # ---------------------------
    #for m_idx in range(6):
    # TODO: I really need to work on my python skills, this is UGLY
    # Draw the header
    cal_start_x = xy[0]
    cal_start_y = xy[1]

    if flagFull:
        hfontsize = 18
        hlineheight = 18
        dfontsize = 11
        dw = (page_width/2.0 - 2*gutter_width)/7.0
        dh = (page_height/2.0 - 2.0*gutter_width - hlineheight)/5.0
    else:
        hfontsize = 12
        hlineheight = 12
        dfontsize = 6
        dw = day_width
        dh = day_width

    # Print the month name (abbr)
    plt.annotate(calendar.month_name[month],
                 xy=(cal_start_x + dw*3.5, -(cal_start_y + hlineheight*0.5)),
                 xycoords='data',
                 horizontalalignment='center', verticalalignment='center',
                 fontsize=hfontsize,
                 color='#ee3300')

    # Print the weekdays (abbr)
    #for idx, day in enumerate(calendar.day_abbr):
    #    # color the day based on whether it is a weekday or not
    #    if idx < 5:
    #        clr = color_workday
    #    else:
    #        clr = color_weekend
    #    #print(idx,day) # TODO: DEBUG
    #    plt.annotate(day,
    #                 xy=(cal_start_x + (idx*dw) + dw/2.0, -(cal_start_y + hlineheight*1.5)),
    #                 xycoords='data',
    #                 horizontalalignment='center', verticalalignment='center',
    #                 fontsize=hfontsize,
    #                 color=clr)

    # Print the month calendar
    for w_idx, week in enumerate(c):
        plt.plot([cal_start_x, cal_start_x+dw*7], [-(cal_start_y + hlineheight*1 + (w_idx+1)*dh), -(cal_start_y + hlineheight*1 + (w_idx+1)*dh)], '#B3BEC7', linewidth=0.5)
        for d_idx, day in enumerate(week):
            # color the day based on whether it is a workday or not
            if d_idx > 4:
                clr = color_weekend
            else:
                clr = color_workday
            # If it is a real day, print it
            if day:
                ###if day == 1:
                ###    print('changing {} to ❶'.format(day))
                ###    day = '❶'
                ###    day = '🕯'
                print('{:3} '.format(day), end='')
                xy = (cal_start_x + (d_idx*dw) + dw*1.0,
                      -(cal_start_y + hlineheight*1.2 + w_idx*dh))
                plt.annotate(day,
                             xy=xy,
                             xycoords='data',
                             horizontalalignment='right', verticalalignment='top',
                             fontsize=dfontsize,
                             color=clr)
        print()

    return (-xy[1] + dh)

def printMonth(year, month):
    '''Print the month calendar in text form for debugging purposes.'''

    # Create the calendar object
    c = calendar.monthcalendar(year, month)

    # Print the header
    print(calendar.month_abbr[month])
    #for day in calendar.day_name:
    for day in calendar.day_abbr:
        print('{:3} '.format(day), end='')
    print()
    # Print the month calendar
    for week in c:
        for day in week:
            # If it is a real day, print it
            if day:
                print('{:3} '.format(day), end='')
            # Otherwise leave it blank but still print
            else:
                print('{:3} '.format(''), end='')
        print()



# TODO: Populate the calendar with important dates
# TODO: Mark dates by category (holiday, birthday, work event, etc.)

# TODO: Save to file (png, svg, pdf - whatever prints best)

# Run the Main program
if __name__ == "__main__":
    import datetime
    import argparse

    # Set up fonts
    import matplotlib
    # Set sans-serif font
    matplotlib.rcParams['font.sans-serif'] = "Fira Code"
    matplotlib.rcParams['font.sans-serif'] = "Calibri"
    # ALWAYS use sans-serif fonts
    matplotlib.rcParams['font.family'] = "sans-serif"

    # Load up events
    # TODO: dynamically control what events get loaded
    import json
    with open('birthdays.json') as json_file:
        data = json.load(json_file)
        for e in data['events']:
            #json.dumps(e, indent=2)
            print('{}: {}'.format(e['type'], e['title']))
    exit()

    # TODO: Learn the right way to set up "usage"
    parser = argparse.ArgumentParser()
    ###parser = argparse.ArgumentParser(
    ###    usage="usage: %prog [options]",
    ###    description='Generates a calendar for a half-page planner.')
    parser.add_argument("-m", "--month",
                        type=int,
                        dest="month",
                        default=None,
                        help="Initial month to print")
    parser.add_argument("-y", "--year",
                        type=int, # optional because action defaults to "store"
                        dest="year",
                        default=None,
                        help="Initial year to print")
    args = parser.parse_args()
    print(args) # TODO: DEBUG

    # If "month" or "year" are not provided, default to the current
    # month and/or year.
    if (args.month is None) or (args.year is None):
        print('Not all inputs provided')
        dt = datetime.datetime.now()
        if args.month is None:
            args.month = dt.month
        if args.year is None:
            args.year = dt.year

    print(' year = {}, month = {}'.format(args.year, args.month)) # TODO: DEBUG

    # Generate the page
    fig = generatePageFigure()

    # Draw the current and next month large on one half-page
    cy = plotMonth(args.year, args.month, fig, (gutter_width, gutter_width), True)
    print('*** {}'.format(cy))

    # TODO: Make function to protect against going past end of year
    #plotMonth(args.year, args.month+1, fig, (gutter_width, page_height/2.0), True)
    cy = plotMonth(args.year, args.month+1, fig, (gutter_width, cy + gutter_width), True)

    # Draw the next 6 months small on the other half-page
    row = 0
    # TODO: Keep track of calendar heights? or use math here
    cal_height = 200
    cy1 = gutter_width
    cy2 = gutter_width
    cgap = 12
    for i in range(2,10):
        m = args.month + i
        if m > 12:
            m = m-12
            y = args.year+1
        else:
            y = args.year
        print(y, m)
        if i % 2:
            # Plot it
            #printMonth(y, m) # TODO: DEBUG
            ##plotMonth(y, m, fig, (page_width/2.0 + page_width/4.0 + gutter_width*0.5,
            ##                      gutter_width + row*cal_height))
            cy2 = plotMonth(y, m, fig, (page_width/2.0 + page_width/4.0 + gutter_width*0.5,
                                  cy2))
            cy2 = cy2 + cgap
            row = row + 1
        else:
            #printMonth(y, m) # TODO: DEBUG
            ##plotMonth(y, m, fig, (page_width/2.0 + gutter_width, gutter_width + row*cal_height))
            cy1 = plotMonth(y, m, fig, (page_width/2.0 + gutter_width, cy1))
            cy1 = cy1 + cgap

    plt.show()
    # TODO: DEBUG plt.savefig(outputname, dpi=80)
    ### TODO: DEBUG plt.savefig('calendar.png', bbox_inches='tight')
    ### TODO: DEBUG plt.savefig('calendar.png', bbox_inches=0)

    # TODO: DEBUG - Show list of all available fonts
    ###import matplotlib.font_manager
    ###code = "\n".join([font for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])
    ###print(code)
