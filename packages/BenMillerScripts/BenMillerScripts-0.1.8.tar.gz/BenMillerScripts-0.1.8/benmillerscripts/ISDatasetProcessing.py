'''Code to process IS Camera Video Datasets in GMS. 

Requires Scipy
To install packages like scipy, see instructions in GMS Help:Python:Installation and Configuration:Additional Packages
Code written by Ben Miller. Last Updated July 2024
'''
import numpy as np
import DigitalMicrograph as DM
import os
import sys
import time
if not DM.IsScriptOnMainThread(): print('Scipy scripts cannot be run on Background Thread.'); exit()
from scipy import ndimage
from tkinter import *
sys.argv.extend(['-a', ' '])
import tkinter.filedialog as tkfd
from numpy.lib.stride_tricks import as_strided
import tqdm
import traceback
import scipy.fftpack
#User-Set Parameters
num_frames_avg = 1
ProcessedName = "Simple Sum of "
result_text_freq = 20
GUI_Progress_Bar = True

output_calibration_0 = None
output_calibration_1 = None
output_calibration_i = None
reciprocal_space_output = False
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Use TQDM??
if GUI_Progress_Bar: 
    from  tqdm.gui import tqdm
    import matplotlib.pyplot as plt
else: 
    #If we don't use the GUI version of the progress bar, don't use tqdm at all.
    tqdm = lambda input: input
    
#Function to process FFT data
def processimage(numpy_data):   
    result = numpy_data
    return result, len(result.shape)

#Function to Get List of All Files in In-Situ Dataset
def BrowseForFileList():
    # Let User Select the IS Dataset Directory
    sys.argv.extend(['-a', ' '])
    root = Tk()
    root.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    dirname = tkfd.askdirectory(parent=root, initialdir=currdir, title='Please select the IS Dataset Root Directory')
    if len(dirname) > 0:
        print("\nOriginal IS DataSet Directory: %s" % dirname)
        newdir=dirname[:3] + 'DMScript Edited Datasets/' + dirname[3:]
        os.chdir(dirname)
    else:
        root.destroy()
        print("User Canceled File Dialog")
        exit()
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith('.dm4')]
    listOfFiles.sort()
    root.destroy()
    return (listOfFiles,dirname,newdir)

def Get_IS_File_List(dirname):
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith('.dm4')]
        listOfFiles.sort()
    return listOfFiles

def DM_interaction_wait_dialog(instructions_str, title_str='DM_Interaction_Dialog',button1_str='Continue',button2_str='Cancel' ):
    '''
    Function to Create a tkinter dialog that enables the user to interact with GMS
    while the script is paused, and then resume the script after they are done
    Accepts:
        instructions_str    string giving instructions to the user about what actions are expected in GMS
        title_str            optional string for the dialog window title
        button1_str            optional string to change the continue button label text
        button1_str            optional string to change the cancel button label text
    Returns: Nothing
    '''
    root = Tk()
    root.attributes('-topmost', 'true')
    root.title(title_str)
    def go_on():
        root.destroy()
    def cancel():
        print("Script Aborted by User")
        root.destroy()
        sys.exit()
    Label(root, text=instructions_str).grid(row=0, sticky=W)
    Button(root, text=button1_str, command=go_on).grid(column=0, row=1, sticky=W, pady=4)
    Button(root, text=button2_str, command=cancel).grid(column=1, row=1, sticky=W, pady=4)
    mainloop()
    

#Function to show an image as a lineplot with better defaults
def display_DM_lineplot(image, 
        name=None,
        scale_y=1,
        origin_y = 0,
        scale_unit_y='a.u.',
        scale_x=1,
        origin_x = 0,
        scale_unit_x='',
        draw_style=1,
        legend=True):
    #Set image name (and thus the lineplot window title)
    if name is None:
        name = "Python LinePlot of "+image.GetName()
    image.SetName(name)
    #set calibration/scale
    image.SetIntensityScale(scale_y)
    image.SetIntensityOrigin(origin_y)
    image.SetIntensityUnitString(scale_unit_y)
    image.SetDimensionCalibration(0,origin_x,scale_x,scale_unit_x,0)
    #Get lineplot display
    image_document = DM.NewImageDocument("")
    image_display = image_document.AddImageDisplay(image,3)
    lineplot_display = DM.GetLinePlotImageDisplay(image_display)
    #Set a few more lineplot parameters
    lineplot_display.SetSliceDrawingStyle(0,draw_style)
    lineplot_display.SetLegendShown(legend)
    #Display Lineplot in DM
    image_document.Show()
    return (image_document, image_display, lineplot_display)
    
def find_ROI(image):
        imageDisplay = image.GetImageDisplay(0)
        numROIs = imageDisplay.CountROIs()
        id = None
        for n in range(numROIs):
            roi = imageDisplay.GetROI(0) 
            if roi.IsRectangle():
                roi.SetVolatile(False)
                roi.SetResizable(False)  
                id = roi.GetID()
                break
        if id is None:
            #If No ROI is found, create one that covers the whole image. 
            print("\nRectangular ROI not found... using whole image")
            data_shape = image.GetNumArray().shape
            roi=DM.NewROI()
            roi.SetRectangle(0, 0, data_shape[0], data_shape[1])
            imageDisplay.AddROI(roi)
            roi.SetVolatile(False)
            roi.SetResizable(False) 
            id = roi.GetID()
            numROIs = 1
        t,l,b,r = roi.GetRectangle()
        text = imageDisplay.AddNewComponent(13, t,l,b,r)  
        text.TextAnnotationSetText(str(numROIs))  
        text.SetForegroundColor(1, 0, 0)
        image.UpdateImage()
        return (id,numROIs)
    
def bin2D(array,binning=(1,1)):
    if binning == 1: 
        return array
    bin=np.flip(binning)
    nh = (array.shape[0]-bin[0])//bin[0]+1
    nw = (array.shape[1]-bin[1])//bin[1]+1
    strides = (array.strides[0],array.strides[1],array.strides[0]*bin[0],array.strides[1]*bin[1])
    shape = (bin[0],bin[1],nh,nw)
    virtual_datacube = as_strided(array,shape=shape,strides=strides)
    result = np.sum(virtual_datacube,axis=(0,1))
    return result

def FFT(array, complex=False):
    if complex: 
        return scipy.fftpack.fftshift(scipy.fftpack.fft2(array))
    else:
        return np.absolute(scipy.fftpack.fftshift(scipy.fftpack.fft2(array)))
    
def MyExpMovingAvg(frame,old_avg,num_frames_sum):
    if num_frames_sum <=1:
        return(frame)
    else:
        persistence = (num_frames_sum-1)/(num_frames_sum+1)
        new_avg = persistence*old_avg + (1-persistence)*frame
        equivalent_sum = new_avg*num_frames_sum
        return(new_avg)

#Getting IS Dataset data
def GetFrontISDatasetInfo():
    image0 = DM.GetFrontImage()
    
    #Get the file path of the dataset open in DM (this needs a one-line DM script)
    dm='GetPersistentTagGroup().TagGroupSetTagAsString("Python_temp:out:FrontFileLocation",GetFrontImageDocument().ImageDocumentGetCurrentFile())'
    DM.ExecuteScriptString(dm)
    (b,filepath) = DM.GetPersistentTagGroup().GetTagAsString('Python_temp:out:FrontFileLocation')
    if os.path.isfile(filepath):
        print(filepath)
    else: 
        print("Front image could not be found on disk. Has it been saved?")
    data_0 = image0.GetNumArray()
    frame_shape = data_0.shape
    assert len(frame_shape) == 2, "This script assumes each in-situ frame is 2D"
    data_type = data_0.dtype
    raw_filepath = filepath[:-4]+".raw"
    folder = os.path.dirname(filepath)
    
    raw_length = 0
    pixels_per_frame = 0
    bytes_per_frame = 0
    listOfFiles = []
    if os.path.isfile(raw_filepath): 
        IS_type = "Director-Raw"
        raw_length = os.path.getsize(raw_filepath)
        pixels_per_frame = np.prod(frame_shape)
        bytes_per_frame = data_0.nbytes
        (b,num_frames) = image0.GetTagGroup().GetTagAsUInt32("In-situ:Recorded:# Frames")
    elif os.path.exists(os.path.join(folder,"Hour_00")): 
        IS_type = "Director-Hybrid"
        (b,num_frames) = image0.GetTagGroup().GetTagAsUInt32("In-situ:Recorded:# Frames")
        listOfFiles = Get_IS_File_List(os.path.join(folder,"Hour_00"))
    else: 
        IS_type = "H-m-s"
        (listOfFiles,dirname,newdir) = BrowseForFileList()
        num_frames = len(listOfFiles)
    print("IS Data Type is: "+IS_type)
    x_origin, x_scale_orig, scale_unit_orig = image0.GetDimensionCalibration(0, 0)
    y_origin, y_scale_orig, scale_unit_orig = image0.GetDimensionCalibration(1, 0)
    origin = (x_origin, y_origin)
    if scale_unit_orig == b'\xb5m': scale_unit_orig = 'um' #scale unit of microns causes problems for python in DM
    return (image0, data_0,
            IS_type, filepath, raw_filepath, folder, listOfFiles,
            frame_shape, data_type, raw_length, pixels_per_frame, bytes_per_frame, num_frames,
            origin, x_scale_orig, y_scale_orig, scale_unit_orig )

class CListen(DM.Py_ScriptObject):
    def __init__(self, img):
        try:
            self.stop = 0
            DM.Py_ScriptObject.__init__(self)
        except: print(traceback.format_exc())
    #Function to end Image Listener
    def __del__(self):
        #global listener
        #if listener in globals(): listener.UnregisterAllListeners()
        print("Script Ended")
        DM.Py_ScriptObject.__del__(self)
        #exit()
    #Function to end script if source image window is closed
    def HandleWindowClosedEvent(self, event_flags, window):
        if not self.stop:
            self.stop = 1
            global listener
            print("Window Closed")
            DM.DoEvents()
            #Unregister all listeners
            #listener.UnregisterAllListeners()
            if GUI_Progress_Bar: plt.close('all')
            print("Processing Script Ended")
            #exit()
    #Function to end script if the ROI is deleted
    def HandleROIRemovedEvent(self, img_disp_event_flags, img_disp, roi_change_flag, roi_disp_change_flags, roi):
        if not self.stop:
            self.stop = 1
            global listener
            print("ROI Removed")
            DM.DoEvents()
            #Unregister all listeners
            #listener.UnregisterAllListeners()
            if GUI_Progress_Bar: plt.close('all')
            print("Processing Script Ended")
            #exit()
            
#Function to get the currently used version of DigitalMicrograph 
def get_DM_version():
    #No Python script command exists to get the DM version, 
    #so we first run a DM script to put the values in the global tags
    dm_script = ('number minor, major, bugVersion\n'
        'GetApplicationVersion(major, minor, bugVersion)\n'
        'GetPersistentTagGroup().TagGroupSetTagAsLong("Python_Temp:DM_Version_Major",major)\n'
        'GetPersistentTagGroup().TagGroupSetTagAsLong("Python_Temp:DM_Version_Minor",minor)\n'
        'GetPersistentTagGroup().TagGroupSetTagAsLong("Python_Temp:DM_Version_bugVersion",bugVersion)')
    DM.ExecuteScriptString(dm_script)
    #Now get the information stored in the global tags by the DM script
    version = [0,0,0]
    _,version[0] = DM.GetPersistentTagGroup().GetTagAsString("Python_Temp:DM_Version_Major")
    _,version[1] = DM.GetPersistentTagGroup().GetTagAsString("Python_Temp:DM_Version_Minor")
    _,version[2] = DM.GetPersistentTagGroup().GetTagAsString("Python_Temp:DM_Version_bugVersion")
    return version  
    

    
    
def modify_calibrations(x_scale_orig,scale_unit_orig, y_scale_orig=None, scalefactor = 1):
        if output_calibration_0 is not None:
            x_scale = output_calibration_0
        else: 
            x_scale = x_scale_orig * scalefactor
            
        if output_calibration_1 is not None:
            y_scale = output_calibration_1
        elif  y_scale_orig is None:
            y_scale = x_scale_orig * scalefactor
        else:
            y_scale = y_scale_orig * scalefactor
            
        if reciprocal_space_output == True:
            scale_unit_x = "1/"+scale_unit_orig
            scale_unit_y = "1/"+scale_unit_orig
        elif scale_unit_orig is None:
            scale_unit_x = " "
            scale_unit_y = " "
        else:
            scale_unit_x = scale_unit_orig
            scale_unit_y = scale_unit_orig
        print(scale_unit_x) 
        print(scale_unit_y)
        return (x_scale, y_scale, scale_unit_x, scale_unit_y)

def ProcessFrontISDataset():
    #Check that we are not running 3.5.0 or 3.5.1 which have a known bug affecting this script.
    if ((get_DM_version()[1] == '51') or (get_DM_version()[1] == '50')):
        DM.OkDialog("Due to a bug in DigitalMicrograph 3.5.0 and 3.5.1, this script would cause DM to crash in those versions. \n\nScript Aborted.")
        exit()
    #Get front image in GMS        
    img1 = DM.GetFrontImage()
    #Get the image window, so we can check if it gets closed
    imageDoc = DM.GetFrontImageDocument()
    imDocWin = imageDoc.GetWindow()
    #Get the image display, for the ROI-removed listener
    imageDisplay = img1.GetImageDisplay(0)

    #Listeners are started here
    #initiate the image listener
    listener = CListen(img1)
    #check if the source window closes
    WindowClosedListenerID = listener.WindowHandleWindowClosedEvent(imDocWin, 'pythonplugin')
    #check if the ROI has been deleted
    ROIRemovedListenerID = listener.ImageDisplayHandleROIRemovedEvent(imageDisplay,'pythonplugin')
   
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    try: 
        (image0, data_0,IS_type,filepath,raw_filepath,folder,listOfFiles,frame_shape,data_type,raw_length,pixels_per_frame,bytes_per_frame,num_frames,origin, x_scale_orig, y_scale_orig, scale_unit_orig )=GetFrontISDatasetInfo()
    except: 
        print(traceback.format_exc())
        print("Failedd ")
        del listener
    #Get the data from the region within an ROI     
    (roi_id,n_rois) = find_ROI(image0)
    roi = DM.GetROIFromID(roi_id)
    val, val2, val3, val4 = roi.GetRectangle()
    data = image0.GetNumArray()[int(val):int(val3),int(val2):int(val4)]
    #get the shape and calibration of the original image, cropped to ROI
    (input_sizex, input_sizey) = data.shape
    (processedimagedata, dims) = processimage(data)

    #create 1st result image
    if dims == 0:
        result_im = DM.CreateImage(np.zeros((1,num_frames)))
        (result_doc, result_disp, result_lpdisp) = display_DM_lineplot(result_im, 
            name=ProcessedName+" ["+str(n_rois)+"] "+image0.GetName(),
            scale_y=1,
            origin_y = 0,
            scale_unit_y='counts',
            scale_x=1,
            origin_x = 0,
            scale_unit_x='frames',
            draw_style=1,
            legend=False)
        raw_out_path = os.path.join(folder,result_im.GetName())+"_0D.raw"
    
    if dims == 1:
        #result_im is a 2D result with each 1D processing result stored as 1 column
        result_im = DM.CreateImage(np.zeros((max(processedimagedata.shape),num_frames)))
        x_scale, y_scale, scale_unit_x, scale_unit_y = modify_calibrations(x_scale_orig,scale_unit_orig, y_scale_orig)
        result_im.SetDimensionCalibration(1,0,x_scale,scale_unit_x,0)
        result_im.ShowImage()
        #Set the image name which will be displayed in the image window's title bar
        result_im.SetName(ProcessedName+" ["+str(n_rois)+"] "+image0.GetName())
        raw_out_path = os.path.join(folder,result_im.GetName())+"_1D.raw"
    if dims == 2:
        result_im = DM.CreateImage(processedimagedata.copy())
        result_im.ShowImage()
        raw_out_path = os.path.join(folder,ProcessedName+" ["+str(n_rois)+"] "+image0.GetName())+"_2D.raw"

    j=0

    if os.path.exists(raw_out_path):
        message = str(raw_out_path) + " Already exists\n Overwrite existing processed data?"
        if not DM.OkCancelDialog(message): exit()
        print("Over-writing existing processed data")
        os.remove(raw_out_path)
    with open(raw_out_path, "ab") as raw_file:
        for i in tqdm(range(num_frames)):
            if listener.stop == 1: break
            if IS_type == "Director-Raw":
                read_start = i*bytes_per_frame - j*raw_length
                if read_start + bytes_per_frame > raw_length:
                    j=j+1
                    count_1 = int((raw_length-read_start)/bytes_per_frame*pixels_per_frame)
                    count_2 = pixels_per_frame-count_1
                    array_1 = np.fromfile(raw_filepath, dtype=data_type, count=count_1, sep='', offset=read_start)
                    raw_filepath = os.path.splitext(raw_filepath)[0]+".raw_"+str(j)
                    print(raw_filepath)
                    array_2 = np.fromfile(raw_filepath, dtype=data_type, count=count_2, sep='', offset=0)
                    array = np.concatenate([array_1,array_2])
                else:
                    array = np.fromfile(raw_filepath, dtype=data_type, count=pixels_per_frame, sep='', offset=read_start)
                frame = array.reshape(frame_shape)
                assert len(frame.shape) == 2, "This script assumes each in-situ frame is 2D"
            if IS_type == "Director-Hybrid":
                image = DM.OpenImage(listOfFiles[i])
                frame = image.GetNumArray()
                assert len(frame.shape) == 2, "This script assumes each in-situ frame is 2D"
                DM.DoEvents()
            if IS_type == "H-m-s": 
                image = DM.OpenImage(listOfFiles[i])
                frame = image.GetNumArray()
                assert len(frame.shape) == 2, "This script assumes each in-situ frame is 2D"
            if i%result_text_freq == 0: 
                print("Processing Frame: %s of %s" %(i,num_frames))
                result_im.UpdateImage()
                DM.DoEvents()
            #val, val2, val3, val4 = roi.GetRectangle() this can be uncommented if you want the ROI to be moveable during processing
            old_avg = data
            data = frame[int(val):int(val3),int(val2):int(val4)]
            data = MyExpMovingAvg(data,old_avg,num_frames_avg)
            (processedimagedata, dims) = processimage(data)
            if dims == 0: result_im.GetNumArray()[0,i] = processedimagedata
            if dims == 1: 
                result_im.GetNumArray()[:,i] = processedimagedata
                raw_file.write(processedimagedata.tobytes())
            if dims == 2:
                if (i%result_text_freq == 0): result_im.GetNumArray()[:] = processedimagedata
                raw_file.write(processedimagedata.tobytes())
            if IS_type != "Director-Raw":
                del image


    if dims == 0:
        os.remove(raw_out_path)
        result_im.UpdateImage()
        DM.DoEvents()
        result_im.SaveAsGatan(os.path.join(folder,result_im.GetName()))
        dm  = "InSituTags_CopyRecordTags(FindImageByID("+str(image0.GetID())+"),FindImageByID("+str(result_im.GetID())+"))"
        dm += "\n FindImageByID("+str(result_im.GetID())+").IMDSetFunctionInSituProfile()"
        DM.ExecuteScriptString(dm)
        DM.DoEvents()
        path_0D = os.path.join(folder,result_im.GetName())+".dm4"
        result_im.SaveAsGatan(path_0D)
        print("Saved 1D Result")
        #Must close and re-open in-situ director image (using an image document) to get the In-Situ Player to sync it
        DM.DeleteImage(result_im)
        print("Opening IS Profile")
        DM.DoEvents()
        doc = DM.NewImageDocumentFromFile(path_0D)
        doc.Show()
        print("Done")
    if dims == 1: 
        #1D IS Dataset
        result_1D = DM.CreateImage(processedimagedata)
        x_scale, y_scale, scale_unit_x, scale_unit_y = modify_calibrations(x_scale_orig, scale_unit_orig, y_scale_orig,)
        result_1D.SetDimensionCalibration(0,0,x_scale,scale_unit_x,0)
        result_1D.SetName(ProcessedName+" ["+str(n_rois)+"] "+image0.GetName()+"_1D")
        result_1D.ShowImage()
        dm  = "InSituTags_CopyRecordTags(FindImageByID("+str(image0.GetID())+"),FindImageByID("+str(result_1D.GetID())+"))"
        dm += "\n FindImageByID("+str(result_1D.GetID())+").IMDSetFunctionInSituDirector()"
        dm += "\n InSituTags_SetRawDataInfo(FindImageByID("+str(result_1D.GetID())+"),FindImageByID("+str(result_1D.GetID())+"))"
        DM.ExecuteScriptString(dm)
        DM.DoEvents()
        path_1D = os.path.join(folder,result_1D.GetName())+".dm4"
        #result_1D.SaveAsGatan(os.path.join(folder,result_1D.GetName()))
        result_1D.SaveAsGatan(path_1D)
        print("Saved 2D and 1D Results")
        #Must close and re-open in-situ director image (using an image document) to get the In-Situ Player to sync it
        DM.DeleteImage(result_1D)
        print("Opening 1D Director Image")
        DM.DoEvents()
        #doc = DM.NewImageDocumentFromFile(os.path.join(folder,result_1D.GetName())+".dm4")
        doc = DM.NewImageDocumentFromFile(path_1D)
        doc.Show()
        print("Done")
    if dims == 2: 
        DM.DeleteImage(result_im)
        #2D IS Dataset
        result_2D = DM.CreateImage(processedimagedata)
        scalefactor = frame_shape[0]/processedimagedata.shape[0]
        x_scale, y_scale, scale_unit_x, scale_unit_y = modify_calibrations(x_scale_orig, scale_unit_orig, y_scale_orig, scalefactor=scalefactor)
        result_2D.SetDimensionCalibration(0,0,x_scale,scale_unit_x,0)
        result_2D.SetDimensionCalibration(1,0,y_scale,scale_unit_y,0)
        result_2D.SetName(ProcessedName+" ["+str(n_rois)+"] "+image0.GetName()+"_2D")
        result_2D.ShowImage()
        dm  = "InSituTags_CopyRecordTags(FindImageByID("+str(image0.GetID())+"),FindImageByID("+str(result_2D.GetID())+"))"
        dm += "\n FindImageByID("+str(result_2D.GetID())+").IMDSetFunctionInSituDirector()"
        dm += "\n InSituTags_SetRawDataInfo(FindImageByID("+str(result_2D.GetID())+"),FindImageByID("+str(result_2D.GetID())+"))"
        DM.ExecuteScriptString(dm)
        DM.DoEvents()
        path_2D = os.path.join(folder,result_2D.GetName())+".dm4"
        #result_2D.SaveAsGatan(os.path.join(folder,result_2D.GetName()))
        result_2D.SaveAsGatan(path_2D)
        print("Saved 2D Results")
        #Must close and re-open in-situ director image (using an image document) to get the In-Situ Player to sync it
        DM.DeleteImage(result_2D)
        print("Opening 2D Director Image")
        DM.DoEvents()
        #doc = DM.NewImageDocumentFromFile(os.path.join(folder,result_2D.GetName())+".dm4")
        doc = DM.NewImageDocumentFromFile(path_2D)
        doc.Show()
        print("Done")
    del image0
    if GUI_Progress_Bar: plt.close('all')