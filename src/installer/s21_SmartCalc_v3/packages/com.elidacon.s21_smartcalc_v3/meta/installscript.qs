function Component()
{
    component.loaded.connect(this, addShortcutCheckBox);
}

addShortcutCheckBox = function()
{
    if (installer.isInstaller()) {
        installer.addWizardPageItem(component, "ShortcutCheckBoxForm", QInstaller.TargetDirectory)
    }
}

Component.prototype.createOperations = function()
{
    component.createOperations();
    var isShortcutChecked = false;
    if (component.userInterface("ShortcutCheckBoxForm")) {
        isShortcutChecked = component.userInterface("ShortcutCheckBoxForm").shortcutCheckBox.checked;
    }
    if (isShortcutChecked) {
        var programName = installer.value("Name");
        if (systemInfo.kernelType == "linux") {
            component.addOperation("CreateDesktopEntry", 
                                    "@HomeDir@/.local/share/applications/"+programName+".desktop", 
                                    "Type=Application\nTerminal=false\nExec=@TargetDir@/"+programName+"\nName="+programName);
            component.addOperation("Copy", "@HomeDir@/.local/share/applications/"+programName+".desktop", "@HomeDir@/Desktop/"+programName+".desktop");
        } else if (systemInfo.kernelType == "winnt") {
            component.addOperation("CreateShortcut", "@TargetDir@/"+programName, "@StartMenuDir@/"+programName+".lnk",
                "workingDirectory=@TargetDir@", "iconPath=%SystemRoot%/system32/SHELL32.dll",
                "iconId=2", "description=Open "+programName);
        }
    }
}
