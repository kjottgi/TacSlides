package Scenes;

import Frames.Frame;

import java.util.ArrayList;

/**
 * Class Frame.
 *
 * Basic Frame Class to encapsulate Frames
 *
 *
 */
public abstract class Scene
{
    private ArrayList frames = new ArrayList<Frame>(); //the frames stored in this scene
    public static Integer number_of_scenes = 0; //the number of scenes made
    private String name; //The name of the current scene.

    public Scene(){


        number_of_scenes = number_of_scenes++; // The number of total scenes has been updated as there is another one.
        this.name = "Scene Number:" + number_of_scenes.toString(); // The name of the scene is the current number


    }

    public void changeName(String new_name)
    {
        this.name = new_name;
    }
    public Frame getFrame(Integer frame){}







}