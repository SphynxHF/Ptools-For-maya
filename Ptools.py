#this script is far from complete, but its a good starting place if you plan on learning Python, or even just a tool to use
#the script is very heavily commented so you can scroll through and see what each item does.
#please dont remove original credits (ofc if you improve it feel free to add yourself! and share it... just dont sell it..)

import maya.cmds as cmds

# Check if the window is open
if cmds.window('window', exists=True):
    # If the window is open, delete it
    cmds.deleteUI('window')
    
# Create a new window
window = cmds.window(title="Ptools")

# Create a layout for the window
layout = cmds.columnLayout()

# Create a new layout for the buttons
buttonLayout = cmds.columnLayout(columnAttach=("both", 5), rowSpacing=10, columnWidth=250)

group1 = cmds.frameLayout(label="Grouping Tools", collapsable=True)

# Create the ungroup button
cmds.button(label="Ungroup", command=lambda *args: unGroupOpjects())

# Create a button to group the selected objects
cmds.button(label="Group", command=lambda *args: groupObjects())

# Create a new button to parent the selected objects
cmds.button(label='Parent', command=lambda *args: parentObjects())

# Create a new button to parent the selected objects
cmds.button(label='Un-Parent', command=lambda *args: unParentObjects())

group2 = cmds.frameLayout(label="Scale Tools", collapsable=True)

# Create a button to double the size of the selected objects
cmds.button(label="Double Size", command=lambda *args: doubleSize())

# Create a button to double the size of the selected objects
cmds.button(label="Half Size", command=lambda *args: halfSize())

# Add a label for the X scale slider
cmds.text(label='X:')

# Create a float slider for the X scale of the objects
xScaleSlider = cmds.floatSliderGrp(min=0.1, max=2.0, value=1.0, step=0.1, changeCommand=lambda *args: updateScale())

# Add a label for the Y scale slider
cmds.text(label='Y:')

# Create a float slider for the Y scale of the objects
yScaleSlider = cmds.floatSliderGrp(min=0.1, max=2.0, value=1.0, step=0.1, changeCommand=lambda *args: updateScale())

# Add a label for the Z scale slider
cmds.text(label='Z:')

# Create a float slider for the Z scale of the objects
zScaleSlider = cmds.floatSliderGrp(min=0.1, max=2.0, value=1.0, step=0.1, changeCommand=lambda *args: updateScale())


group3 = cmds.frameLayout(label="History Tools", collapsable=True)

# Create a button to freeze transforms, center the pivot, and delete all history
cmds.button(label="Freeze and Delete History", command=lambda *args: freezeAndDelete())

group4 = cmds.frameLayout(label="Retopology Tools", collapsable=True)

# Create a button to remesh and retopologize the selected objects
cmds.button(
    label="Remesh and Retopologize", command=lambda *args: remeshAndRetopologize()
)

# Create a button to retopologize the selected objects at 15000
cmds.button(label="Retopologize 15000 Poly", command=lambda *args: retopologize15000())

# Create a button to retopologize the selected objects at 7500
cmds.button(label="Retopologize 7500 Poly", command=lambda *args: retopologize7500())

# Create a button to retopologize the selected objects at 3750
cmds.button(label="Retopologize 3750 Poly", command=lambda *args: retopologize3750())

# Create a button to retopologize the selected objects at 1875
cmds.button(label="Retopologize 1875 Poly", command=lambda *args: retopologize1875())

group5 = cmds.frameLayout(label="UV Tools", collapsable=True)

# Create a button to AutoProject UV the selected objects at 1875
cmds.button(label='Poly Auto Projection', command=lambda *args: autoProjection())

group6 = cmds.frameLayout(label="About PTools", collapsable=True)

# Create a new button to open the credits window
cmds.button(label='Credits', command=lambda *args: openCredits())

def groupObjects():
    # Get the list of selected objects
    selectedObjects = cmds.ls(selection=True)

    # Check if there are at least two objects selected
    if len(selectedObjects) < 2:
        # If there are not enough objects selected, display an error message
        cmds.confirmDialog(
            title="Error", message="Please select at least 2 objects to group."
        )
        return

    # Group the selected objects
    cmds.group(name="myGroup")


def unGroupOpjects():
    # Get the list of selected objects
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one group selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 group to ungroup."
        )
        return
    cmds.ungroup()

def parentObjects():
    # Get the list of selected objects
    selectedObjects = cmds.ls(selection=True)
    
    # Check if there are atleast one group selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 group to parent."
        )
        return
        # Parent the selected objects
        cmds.parent()

def unParentObjects():
    # Get the list of selected objects
    selectedObjects = cmds.ls(selection=True)
    
    # Check if there are atleast one group selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 group to unparent."
        )
        return
        # Parent the selected objects
        cmds.parent(-w)
    

def doubleSize():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to double size."
        )
        return
    cmds.scale(2, 2, 2, relative=True)


def halfSize():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to half size."
        )
        return
    cmds.scale(0.5, 0.5, 0.5, relative=True)
    
def updateScale():
    # Get the values of the sliders
    xScale = cmds.floatSliderGrp(xScaleSlider, query=True, value=True)
    yScale = cmds.floatSliderGrp(yScaleSlider, query=True, value=True)
    zScale = cmds.floatSliderGrp(zScaleSlider, query=True, value=True)

    # Select the objects
    selectedObjects = cmds.ls(selection=True)
    
    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to resize."
        )
        return
    # Scale the selected objects
    cmds.scale(xScale, yScale, zScale, relative=True)


def freezeAndDelete():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error",
            message="Please select atleast 1 object to freeze and delete history on.",
        )
        return
    # Freeze the transforms of the selected objects
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

    # Delete all history of the selected objects
    cmds.delete(constructionHistory=True)


def remeshAndRetopologize():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Retopo."
        )
        return
    # Remesh the selected objects
    cmds.polyRemesh(tsb=0, smt=50, ipt=2)

    # Retopologize the selected objects
    cmds.polyRetopo(targetFaceCount=15000, preprocessMesh=True)


def retopologize15000():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Retopo."
        )
        return
    # Retopologize the selected objects
    cmds.polyRetopo(targetFaceCount=15000, preprocessMesh=True)


def retopologize7500():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Retopo."
        )
        return
    # Retopologize the selected objects
    cmds.polyRetopo(targetFaceCount=7500, preprocessMesh=True)


def retopologize3750():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Retopo."
        )
        return
    # Retopologize the selected objects
    cmds.polyRetopo(targetFaceCount=3750, preprocessMesh=True)


def retopologize1875():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Retopo."
        )
        return
    # Retopologize the selected objects
    cmds.polyRetopo(targetFaceCount=1875, preprocessMesh=True)
   
def autoProjection():
    selectedObjects = cmds.ls(selection=True)

    # Check if there are atleast one object selected
    if len(selectedObjects) < 1:
        cmds.confirmDialog(
            title="Error", message="Please select atleast 1 object to Auto-Project."
        )
        return
    # Auto-Project the selected objects
    cmds.polyAutoProjection()

def openCredits():
    # Create a new window for the credits
    creditsWindow = cmds.window(title='Credits')

    # Create a layout for the credits information
    creditsLayout = cmds.columnLayout()

    # Add a label with the creator information
    cmds.text(label='Created by: Michael Hite')

    # Add a label with the contact information
    cmds.text(label='Email: Mike.p.hite@gmail.com')
    
    # Add a label with the discord contact information
    cmds.text(label='Discord: Sphynx#7106')
    
    # Add a hyperlink to the website
    cmds.text(l='<a href="https://8bitplane.com/">Visit 8bitplane website</a>',
hl=True)
    # Show the window
    cmds.showWindow(creditsWindow)

# Show the window
cmds.showWindow(window)
