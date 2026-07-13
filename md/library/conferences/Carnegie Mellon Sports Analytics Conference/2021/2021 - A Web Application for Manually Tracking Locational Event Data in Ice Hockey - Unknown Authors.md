<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2021/2021 - A Web Application for Manually Tracking Locational Event Data in Ice Hockey - Unknown Authors.pdf -->

# A Web Application for Manually Tracking Locational Event Data in Ice Hockey 

### An Nguyen<sup>_∗_</sup> 

#### **Abstract** 

Sometimes, sports data must be tracked by hand, as desired data may not be available through existing sources, if it exists at all. But, manual tracking is often tedious and hard to translate into a useful form for analysis. In ice hockey, manual tracking is often especially necessary in women’s and youth ice hockey as data is often sparser and more difficult to access in those competitions. To aid the process of manual tracking in ice hockey and encourage an increase in the breadth and depth of data available, this work describes an open-source web application designed to reduce the hardships of manually tracking locational event data in ice hockey. The web application distinguishes itself from similar applications by its user-friendliness and high level of customizability. By clicking on a location on a rink, the corresponding coordinates of that event are logged as a table row. Details in additional columns in the table are recorded using a details panel beside the rink. The data is downloadable in `.csv` format for further exploration and analysis. New details can be created with corresponding widgets in the details panel and columns in the table. The application also provides the ability to record one or two sets of coordinates per event, for tracking events where start and end locations are desired. These custom setups of the application with new details and options can be saved and later loaded into the web application, saving time recreating the environment. 

## **1 Introduction** 

### **1.1 What is the Web Application?** 

The web application (shot-plotter.netlify.app) provides a graphical interface for creating a table of events occurring during an ice hockey game. Coordinates are logged by clicking on the appropriate location on a rink. Additional details about the event are recorded in a details panel beside the rink using form elements like radio buttons, text fields, and dropdowns. The event table is then downloadable in `.csv` format. The app is currently known as _Shot-Plotter_ due to its original and default purpose of plotting shots; however, its customizability enables tracking any events and associated details with ease. 

### **1.2 Prior Work** 

Over the past few years, there have been various web applications with the same core idea of providing a graphical interface of a clickable rink for logging locational events in ice hockey. 

At the start of 2018, the now-defunct tracking system, _Tape to Tape_ was released by Rushil Ram in conjunction with hockey analytics website Meta Hockey [1]. _Tape to Tape_ was specifically designed for tracking passes, zone entries, and zone exits in the NHL. _Tape to Tape_ had unique features catered to that purpose like integration with the NHL play-by-play data, but was not accomodating to other use cases. 

In late 2018, inspired by a podcast comment by Alyssa Longmuir about useful tools for a "’grassroot’ analytics league" outside of the NHL, Andrew Pucci released _ShotPlot_ [3]. _ShotPlot_ [6] hones in on the location-recording aspect of tracking events: the application allows custom units of measurement (i.e. feet, meters, etc.) and provides the ability to toggle between the different specifications of a North American rink and an international rink. However, no additional details about events can be recorded using _ShotPlot_ . 

Longmuir used a mix of hand tracking and _ShotPlot_ for tracking a season of the Australian Women’s Ice Hockey League. But when she wanted to have shot heat maps on hand for helping local teams perform and 

> _∗_ Harvey Mudd College; anguyen@hmc.edu 

1 

schoolchildren get into sports analytics, Longmuir developed her own application, _Hockey Plotter_ in late 2020 [4]. _Hockey Plotter_ [5] is a Shiny application that features a rink to plot shots or goals, as well as radio buttons and a text field to log the team and player of each event, respectively. Its most unique feature was the cause of its creation: by switching tabs in the application, plotted shots are visualized as a heat map. However, a key drawback is the slowness of plotting shots: after clicking on the rink, each shot takes a second or two to appear. 

After using Longmuir’s _Hockey Plotter_ to help digitize shot charts from historical women’s ice hockey Olympics games and being frustrated by the shot-appearance delay, _Shot-Plotter_ was originally released in early April 2021. 

### **1.3 What Makes Shot-Plotter Unique** 

What sets _Shot-Plotter_ apart is two-fold: its ease of use and adaptability. 

The application prioritizes having a straightforward user interface (UI) and having as little friction while using the application as possible. Events appear instantly after clicking on the rink to provide immediate feedback to the user. The UI is responsive, adapting to changes in screen size for compatibility with computers and mobile devices. The application is functional with the default setup, without forcing a need for customization if not desired. If users wish to customize the application, the UI guides the user using form elements, examples, and labels. Documentation is hidden by default to avoid overwhelming the user with information but is available if needed. 

The most noteworthy feature of _Shot-Plotter_ is the degree of customization users have, especially with regards to additional details logged alongside the coordinates. Similar applications have fixed options for information recorded alongside coordinates, while _Shot-Plotter_ allows deleting, reordering, and adding new additional details. Combined with the ability to record two sets of locations per event, _Shot-Plotter_ can be used to track almost any event and associated details imaginable. The application is also agnostic of the league, competition, and level of ice hockey. Theoretically, any event occurring on an ice rink is trackable with _Shot-Plotter_ . 

## **2 The Structure of the Application** 



Figure 1: A screenshot of the _Shot-Plotter_ web application, with the header and footer cropped to save space. A rink (Section 2.1) and a details panel (Section 2.2) to the left occupy most of the space. Below the details panel and rink is a table (Section 2.3) containing one row. Below the table is a section to upload and download the table (Section 2.4). 

2 

### **2.1 Rink** 

Clicking on the rink logs an event. 

The rink matches the NHL rulebook specifications as of the 2021-2022 season [2] and the coordinate system matches that of NHL play-by-play data. The center of the rink has coordinates (0,0). The x-axis is along the length of the rink; x-values range from -100 feet on the left to 100 feet on the right. The y-axis is along the center line of the rink; y-values range from -42.5 feet at the bottom to 42.5 feet at the top. 

When the rink is clicked, a row in the table appears and a dot appears at the clicked location. These comprise a representation of the event logged. Additional details about the event included in the row, as well as the dot’s appearance, are based on the information in the details panel (Section 2.2). 

### **2.2 Details Panel** 

The details panel is where additional details about an event are recorded. 

The details panel is divided into sections called widgets that provide a way to record additional details for each event. When an event is logged by clicking on the rink, the value of the event’s row in each detail column is the current value of the corresponding detail widget. For example, in Figure 1, since the value "Shot" is currently selected in the **Type** widget, if an event were to be logged, the value in the **Type** column would be "Shot". 

The default details, **Period** , **Team** , **Player** , **Type** , were chosen as common information wanted for a shot in ice hockey. The default details (excluding **Period** ) also map to specific visual indicators on the rink. The **Team** and **Type** details control the color and shape of the event’s dot on the rink, respectively; the legend below the rink indicates the corresponding values. The legend updates as the **Team** names are edited and additional options are added to **Type** . If the value in the **Player** widget is two characters or less (intended for indicating a player’s number), the value will appear on the dot. These visual indicators increase the legibility of events just from the rink and minimize the need to cross-reference with the table. For example, in Figure 1, we can determine the logged event on the rink was a "Miss" by "Finland" player number "12" just by looking at the dot. 

### **2.3 Table** 

The table displays the event information in a layout that mimics the downloadable version of the data and allows the highlighting and deletion of events. 

By default, the table has 7 columns: 4 corresponding to the widgets, **Period** , **Team** , **Player** , **Type** , an **X** and **Y** column for the x-coordinate and y-coordinate of the event’s location, and a **#** column indicating the number of the event relative to the other events (i.e. the fifth event logged has value "5" in the **#** column). 

The table is divided into pages of rows; by default, the table shows the last page, which contains the last ten events recorded. The footer of the table indicates the numbers of the currently displayed events on the left-hand side; the right-hand side of the footer shows the current page and has buttons for switching to the previous and next page of the table, if any (Figure 2). 

On the left end of each event’s row in the table, there is a checkbox that is used to highlight that event. When an event is highlighted, its row is colored corresponding to its team, and its dot on the rink enlarges. Multiple events can be highlighted at once (Figure 2). 

There is a trash can icon on the right end of each event’s row. When clicked, that event is deleted: the corresponding row and dot disappear from the table and rink respectively, and the event numbering in the **#** column adjusts if needed. There is also a trash can icon alongside the column names in the table; when clicked, a modal appears asking if the user wants to delete all recorded events. If the user confirms, all rows and dots disappear from the table and the rink. 

### **2.4 Table Download and Upload** 

Below the table is a section where the table can be downloaded in `.csv` format, or the table can be populated by uploading an existing `.csv` . 

Typing into the white text box between the download button changes the file name, though it is always in `.csv` format as indicated at the end. By default, the file name is the date and time when the web app was initially opened. 

3 



Figure 2: A screenshot of the _Shot-Plotter_ web application; the header, footer, and table download and upload functionality are cropped out to save space. Only the 6th through 15th events out of 15 total events are currently displayed in the table, per the footer. There is a button to navigate to the previous page of the table. The table contains two highlighted events. On the rink, the larger size of the highlighted event dots distinguishes between the two "Shot" events by "United States" player "12" on the right half of the rink and between the two "Shot" events by "Finland" player "65" on the left half of the rink, which otherwise would appear identical. 

The downloaded file includes the values in any columns with corresponding widgets in the details panel and any coordinate columns; this means the default **#** column is excluded. The downloaded file includes column names. Figure 3 shows the contents of the downloaded `.csv` file corresponding to the table in Figure 1. 

Files can be uploaded by clicking anywhere on the upload section; files must be in `.csv` format with column names in the file corresponding to the widget and coordinate column names in the web application’s table. When a file is uploaded, any events currently in the app’s table are removed, and then the table and rink populate with rows and dots corresponding to the events in the file. 

```
Period,Team,Player,Type,X,Y
1,Finland,12,Miss,-82.00,6.50
```

Figure 3: Content of a downloaded `.csv` file corresponding to the table in Figure 1. 

### **2.5 Sample Workflow using the Default Application** 

What follows is an example of a possible workflow to illustrate features in action using the default setup of the application. 

4 

Say we are tracking shot events for a game between Sweden and Germany. Before the game starts, we can enter "Sweden" and "Germany" into the name boxes in the **Team** widget; the countries will then appear in the color legend below the rink. We can also add any additional values we want to the **Type** widget to not waste time typing them when they come up in-game. If we wish to distinguish shots through traffic, for example, we can add the value "Traffic" to the **Type** widget by typing it into the dropdown and hitting enter. "Traffic" will then appear as a new option in the dropdown and the shape legend beneath the rink. 

Then, when the game starts, we can track shots as they happen, adjusting the **Player** and **Type** values as necessary in the details panel and then clicking on the matching location on the rink to log the shot. We will likely make mistakes along the way: perhaps we click on the wrong location or forget to adjust one of the details. In that case, we can delete the erroneous shot from the table and then log it again. If we figure out we erred logging an older shot, we can highlight events to ensure we delete the intended one. We can also highlight events throughout the game to keep track of key shots we want to note later. 

Say we get to the break between periods 1 and 2. After switching the **Period** widget value to "2", we might want to save our progress. We can download the shots currently in the table to a `.csv` file, naming it `germany-sweden-period-1.csv` to indicate it is not a complete game tracking. After we download the file, the events are still in the web application table. We can then continue tracking shots in the following periods, adding to the logged shots from period 1. Alternatively, we can use the trash can icon in the table header to delete all current shot events and instead track period 2 using a clean rink and table while preserving our values in the details panel, and then merge the files later. Either way, if anything happens, we can upload our downloaded file to restore all of the tracked events from the first period. 

Then, when the game is over, we can download our `.csv` file(s) and use them for statistical analysis, either by hand or with some other tool. 

## **3 Customizing the Setup of the Application** 

By default, the _Shot-Plotter_ application is aimed at tracking shots. However, by customizing the application’s setup, the app can be tailored to any use case. Customizing the setup can involve changing what additional details are recorded with each event (Sections 3.1 and 3.2), modifying the application’s appearance (Section 3.3), and enabling 2-location events (Section 3.4). These custom setups can be downloaded to a file and restored at a later point by uploading that file (Section 3.5). 

The setup can be customized by clicking on the "Customize Setup" button at the bottom of the details panel. The setup can only be customized when there are no events logged; when events are logged, the "Customize Setup" button turns grey to indicate it is disabled. 

Clicking on the "Customize Setup" button causes a pop-up window to appear (Figure 4). At the top, there is a quick blurb about what options are available, with a "More Info" option that, when clicked, expands to display more detailed instructions on how to achieve everything mentioned. The "Save Changes" button in the bottom right closes the pop-up, returning the user to the main application but with any customizations applied. 

### **3.1 Reordering, Hiding, and Deleting Details** 

Below the informational blurb, there is a row of boxes; each box corresponds to a detail recorded for each event. We can use the boxes to modify these details. 

Dragging and dropping the detail boxes changes the order in which the matching detail widgets appear in the details panel, and the order in which detail columns appear in the table. 

For most detail boxes, there is an eye icon and a trashcan icon. The eye icon indicates that detail is currently visible. By clicking on the eye icon, the corresponding widget and column of that detail are hidden from view and do not appear in the details panel and table respectively. The eye icon will change to an eye with a slash to indicate it is hidden. Clicking on the eye icon will toggle between states of hidden and visible. Clicking on the trash can icon deletes the detail entirely; the detail disappears from the detail boxes, and the detail does not appear in the details panel or table. Coordinate details, like **X** and **Y** , cannot be hidden or deleted. 

For example, say we deleted the **Period** detail, hid the **Type** detail, and reordered the boxes so the **Team** detail came last. Then in the details panel, the **Team** widget would come after the **Player** widget, and the columns in the table would be, in order, **#** , **Player** , **X** , **Y** , **Team** (Figure 5). 

5 



Figure 4: A screenshot of the main view of the customization pop-up window. At the top is information about what can be customized. Below that is a row of boxes corresponding to the details (Section 3.1), then a button to create a new detail (Section 3.2). Below that are some options to modify the appearance of the application (Section 3.3) and a toggle to enable 2-location events (Section 3.4). At the bottom is a section to download and upload a custom setup (Section 3.5). 







Figure 5: The resulting changes to the detail boxes, details panel, and table produced by deleting the **Period** detail, hiding the **Type** detail, and reordering the columns so the **Team** detail comes last (Section 3.1). 

### **3.2 Creating New Details** 

Say we want to record another detail for each event, **Strength** : whether an event occurs at even-strength, during a power play, or during a penalty kill. We can click on the "Create New Detail" button, and the customization pop-up window will switch to a view that describes the different kinds of detail widgets we can make (Figure 6). 

6 



Figure 6: A screenshot of the pop-up window view for selecting what kind of widget to create for a new detail. 

New details can select from four types of widgets: radio buttons, text fields, dropdowns, and countdown/countup timers (known as time widgets). For each widget, the view provides an interactive example and a brief description of ideal use cases. For **Strength** , since we only want three options, the descriptions suggest using radio buttons. We can click on the "Create Radio Buttons" button to switch to another view that guides us through creating our new radio buttons widget. Each widget type has a unique view for creating that widget; but all views have the same structure: an example at the top, a brief description of what is needed, and a form to enter the information for that widget. In our case, we can type "Strength" as the detail name, and enter "EV" (even strength), "PP" (power play), and "PK" (penalty kill) as the options. We will need to add another option, as there are only two by default. We can then select "EV" to be the default selected option (Figure 7). When we click "Create Radio Buttons," we are returned to the initial view of the customization window, but there is now a new detail box, "Strength" with a not-yet-seen pencil icon. The pencil icon allows editing that detail’s widget: clicking it will return us to the radio buttons widget creation view, but the example will match the current widget and the form will be pre-filled appropriate for that widget. When we return to the main web application, we can see our new detail in action as a widget in the details panel and as a column in the table (Figure 8). 

Any number of new details can be created. 

7 



Figure 7: A screenshot of the view for creating a new radio buttons widget. The form is filled out to create a new detail called **Strength** with options "EV", "PP", and "PK". 

### **3.3 Appearance Preferences** 

Below the detail boxes, on the left, there are options to modify the application’s appearance. 

By default, there are two widgets per row in the details panel; this number can be adjusted down to one, for users who want more space per widget, or up to three, for users who have many widgets and want to cut down on the space taken up by the details panel. 

There are ten rows per page of the table by default. The number of rows can range from one row per page, for users who only want to see a single event at a time, all the way to 999, for users who want all events visible. 

### **3.4 2-Location Events** 

Say we want to record an event best described using two locations: for example, passes with a start and endpoint. By enabling 2-location events, we can have two sets of coordinates for a single event 

Enabling the "Enable 2-Location Events" option adds two details representing the coordinates for the new location: **X2** and **Y2** . As coordinate details, they cannot be hidden or deleted. 

When we return to the main web application, besides the new **X2** and **Y2** columns in the table, above the rink there will be a similar toggle with values "1-location" and "2-location" (Figure 9). This toggle indicates what type of event will be created. There are two ways to switch between the modes: the shift button on the keyboard and the toggle above the rink. "2-location" mode is active as long as the shift button is held down; this simplifies actively switching between the two modes. Alternately, clicking the toggle above the rink switches between the two modes. The toggle is useful for being in "2-location" mode for long periods without needing to hold down shift the entire time, and for mobile devices when the shift button is not present or not easily accessible. 

In "1-location" mode, the application works as default, and the **X2** and **Y2** will be empty for all events. In "2-location" mode, clicking on the rink will first create a miniature, less opaque version of the traditional dot at that location. Then, clicking on the rink again will create a dot at this second location, with a line and an arrow connecting the two dots and the normal opacity for both dots (Figure 9). Events are not logged in the table 

8 



<!-- Start of picture text -->
(a) A row of detail boxes featuring the Strength detail.<br>(b) A table featuring the Strength column.<br>(c) A details panel featuring the<br>Strength widget.<br><!-- End of picture text -->





Figure 8: The resulting changes produced by adding the **Strength** detail as described in Section 3.2. 





Figure 9: The stages of logging a two-location event on the rink. The toggle between "1-location" and "2-location" mode above the rink is visible. 

until both locations are marked. The first location, indicated by the smaller dot, has its coordinates in the **X** and **Y** columns, while the second location, indicated by the normal-sized dot, has its coordinates in the **X2** and **Y2** columns. 

### **3.5 Setup Download and Upload** 

By creating new details and deleting and hiding unnecessary ones, changing the application’s appearance, and enabling 2-location events, we can completely customize our setup of the application. However, those changes do not last forever; the application completely resets to default once refreshed to help ensure data privacy. But recreating a custom setup by hand is tedious at best and requires photographic memory at worst. 

Instead, next to the "Save Changes" button in the customization pop-up window, we can download a `.json` file. This file preserves the following information about the application’s current setup: the current values of all widgets in the details panel, appearance preferences, whether 2-location events are enabled, and the order and visibility status of all details, including created details. Then, by uploading that same file at a later point in the upload section, that setup is completely restored. We can rename the file, by default named `custom-setup.json` , by clicking on the text box next to the download button. 

For example, say we wanted to track passes during a series of games involving Finland. Before the series starts, we could make our custom setup. We could enable 2-location events, create any new details like perhaps a 

9 

**Period Time** detail with a time widget, and hide and rearrange the columns. We could then hit "Save Changes" and modify the default values in the details panel, like by making Finland one of the **Team** options and adding any values to **Shot** we want, like whether an event went through "Traffic." Then, we can reopen the customization pop-up window since we haven’t logged any events, and we can download our new custom setup file. Then, when we are about to track a game, we can open _Shot-Plotter_ , open the customization pop-up window, upload that file, and our changes will be restored. This custom setup `.json` file can also be shared with others to maintain a consistent data format for a larger-scale manual tracking project. 

## **4 Conclusion** 

This application provides a user-friendly way to track events in ice hockey. The user interface guides input through form elements and icons, and makes logging events require as few clicks as possible with instant feedback about what was recorded. The application is currently known as _Shot-Plotter_ due to its default setup aimed at tracking shots, but its customizability allows almost any event imaginable to be easily tracked through the creation of custom details and 2-location events. The application benefits from active development: none of the customization features were available at the initial release in early April 2021 and have instead been added over time. There are many more planned features as well, like the ability to filter displayed events for using the rink as a live visualization tool. The application can aid the manual tracking of data in all levels of ice hockey, whether by independent fans and analysts or by ice hockey teams. In addition, the modular nature of the source code (available on GitHub) means the application could be adapted for other sports with relative ease. By swapping out the rink for an appropriately scaled `.svg` of another playing area and changing the default details, stored as a `.json` , the application could be used in other sports without touching the bulk of the code logic. 

By providing an easier way to track locational events, this application hopes to encourage manual tracking of data across leagues and levels, to increase the depth and breadth of high-quality and accessible data in ice hockey and, perhaps in the future, across the sports world in general. 

## **References** 

- [1] Prashanth Iyer. _An Introduction to New Tracking Technology_ . Jan. 2018. url: `https://hockey-graphs. com/2018/01/02/an-introduction-to-new-tracking-technology` . 

- [2] National Hockey League. “Section 1 - Playing Area”. In: _National Hockey League Official Rules 2021-2022_ . 2021. 

- [3] Alyssa Longmuir. _An Australian Hockey Analytics Odyssey_ . The Ice Garden. Jan. 2019. url: `https://www. theicegarden.com/2019/1/27/18185866/analytics-odyssey-womens-hockey-awihl-australiastatistics-analysis-data-tracking` . 

- [4] Alyssa Longmuir. _Building a Shot-Plotting App in Shiny_ . Hockey Graphs. Oct. 2020. url: `https://hockeygraphs.com/2020/10/01/building-a-shot-plotting-app-in-shiny` . 

- [5] Alyssa Longmuir. _Hockey Plotter_ . Version 1.1. url: `https://aklongmuir.shinyapps.io/HockeyPlotter` . 

- [6] Andrew Pucci. _ShotPlot_ . url: `https://shotplot.app` . 

10 


