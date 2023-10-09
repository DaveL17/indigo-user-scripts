## User Scripts Plugin

Install this plugin if you would like to add AppleScript or Python script files to Indigo's Plugins menu.

To install, download the plugin from _releases_ above, unzip it, then double-click the **`User Scripts.indigoPlugin`** 
file to install.

Next, control-click (or right-click) on this file and choose **`Show Package Contents`** from the context menu 
(depending on which version of Indigo you're using):

    /Library/Application Support/Perceptive Automation/Indigo 2022.1/Plugins/User Scripts.indigoPlugin
    /Library/Application Support/Perceptive Automation/Indigo 2022.2/Plugins/User Scripts.indigoPlugin
    /Library/Application Support/Perceptive Automation/Indigo 2023.1/Plugins/User Scripts.indigoPlugin

And then add any AppleScript (.scpt) or Python (.py) files into the folder:

    User Scripts.indigoPlugin/Contents/Menu Items/

Lastly, choose the **`Plugins->User Scripts->Reload Plugin`** menu item.

Your scripts should then be accessible from the **`Plugins->User Scripts`** menu item.
