'''
Set of helper functions to use 
'''
import numpy as np
import pandas as pd
import math



def extract_timestamp_cutouts(trace_to_extr:np.ndarray,uncor_timestamps:np.ndarray,baseline:float, posttime=None,sampling=1,offset=0.0,z_scored=False,dff=False)->pd.DataFrame:
    """
        Arguments:
        trace_to_extract: an array containing values of interest (e.g. dF/F trace), ASSUMES CONSTANT SAMPLING FREQUENCY!!

        timestamps: array containing timepoints of the events, points from trace_to_extract will be taken around each timestamp

        baseline: time before the timepoint (in seconds) to be extracted

        posttime: time after the timepoint (in seconds) to be extracted, by default equals baseline

        sampling: acquisition rate of the trace_to-extract, in Hz (by default 1)

        offset: shift in time in seconds between timestamps and trace_to_extract (if, for example photometry acqusition starts 5 seconds before behavior video 
            from which timepoints were annotated offset = 5)

        z-scored: returns cutouts as z-score values computed on baseline

        dff: returns cutouts as deltaF/F values computed on baseline

        Returns:
        DataFrame with signal cutouts around each trigger, organized in columns
    """
    #Copy the input trace
    trace_to_extract = trace_to_extr.copy()
    #if time after the trigger is not specified, make it equal to baseline
    if not posttime:
        posttime=baseline
    #Make "result" dataframe
    result=pd.DataFrame()
    #Apply offset to trigger timestamps
    timestamps = uncor_timestamps+offset
    #Define length of the cutout (in points)
    cutout_length =  round((posttime+baseline)*sampling)
    #Define time points of the cutouts relative to the trigger
    #result.index=np.round(np.arange(-baseline,posttime,1/sampling),round(math.log10(sampling)+2))

    cutouts = []
    #Extract cutouts around each trigger in a loop
    for i,timestamp in enumerate(timestamps):
        indfrom = round((timestamp-baseline)*sampling)
        if indfrom<0 or indfrom+cutout_length>len(trace_to_extract)-1:
            continue
        cutouts.append(pd.Series(trace_to_extract[indfrom:indfrom+cutout_length]))
        #result["Cutout{}".format(i)]=trace_to_extract[indfrom:indfrom+cutout_length]

    result = pd.concat(cutouts, axis=1)
    result.index=np.round(np.arange(-baseline,posttime,1/sampling),round(math.log10(sampling)+2))
    
    #Apply deltaF/F0 transformation to all cutouts (columns of results
    if dff:
        for col in result:
            base_mean = result.loc[:0,col].mean()
            result[col]-=base_mean
            result[col]/=base_mean
    #Apply deltaF/F0 transformation to the cutout (columns of results)
    if z_scored:
        for col in result:
            std = result.loc[:0,col].std()
            result[col]-=result.loc[:0,col].mean()
            result[col]/=std
            
    return result



def locate_onsets_offsets(annotated_trace:np.ndarray, time_trace:np.ndarray = None, thresh=0.5, on_dur_thresh=0, off_dur_thresh=0)->tuple[np.ndarray, np.ndarray]:
    '''
    
    '''
    if not time_trace:
        time_trace = np.arange(len(annotated_trace))
    onsets = time_trace[(annotated_trace>thresh) & (np.roll(annotated_trace,1)<=thresh)]
    offsets = time_trace[(annotated_trace<thresh) & (np.roll(annotated_trace,1)>=thresh)]
    


    if off_dur_thresh>0:
        off_durations=onsets-np.roll(offsets,1)
        indices_to_remove=np.arange(len(onsets))
        indices_to_remove = indices_to_remove[off_durations<off_dur_thresh][1:]
        onsets=np.delete(onsets,indices_to_remove)
        offsets=np.delete(offsets,indices_to_remove-1)

    if on_dur_thresh>0:
        on_durations=offsets-onsets
        indices_to_remove=np.arange(len(onsets))
        indices_to_remove = indices_to_remove[on_durations<on_dur_thresh]
        onsets=np.delete(onsets,indices_to_remove)
        offsets=np.delete(offsets,indices_to_remove)

    return onsets, offsets




def bin_trace(trace:np.ndarray, binwidth=1, just_smooth=False):
    if binwidth>1:
        numpnts = (len(trace)//binwidth) *binwidth
        trace = np.insert(trace, 0 , [trace[0] for _ in range(binwidth)])
        trace = np.append(trace, [trace[-1] for _ in range(binwidth)])
        new_trace = trace.copy()
        

        for i in range(1,binwidth):
            new_trace+=np.roll(trace,-i)
        if just_smooth:
            return np.roll(new_trace/binwidth,binwidth//2)[binwidth:-binwidth]
        else:
            return new_trace[binwidth:-binwidth][0:numpnts:binwidth]/binwidth
    else:
        return trace