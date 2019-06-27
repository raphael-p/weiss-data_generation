#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk


def main():
    colors = vtk.vtkNamedColors()

    # Create a plane
    planeSource = vtk.vtkPlaneSource()
    planeSource.SetOrigin(0.0, 0.0, 0.0)
    planeSource.SetPoint1(42, 0.0, 0.0)
    planeSource.SetPoint2(0.0, 33, 0.0)
    planeSource.SetNormal(0.0, 0.0, 1.0)
    #planeSource.SetCenter(0.0, 0.0, 0.0)
    planeSource.Update()

    plane = planeSource.GetOutputPort()

    # Save plane to file
    plyWriter = vtk.vtkPLYWriter()
    plyWriter.SetFileName("../data/grid_manual")
    plyWriter.SetInputConnection(plane)
    plyWriter.Write()

    # Create a mapper and actor
    plane = planeSource.GetOutput()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(plane)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d("Cyan"))

    # Create a renderer, render window and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Plane")
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Set the background color.
    colors.SetColor("BkgColor", "white")

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("BkgColor"))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()