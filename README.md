# What is this  
   *  import video, chop them up, and label them  
      to make sample pics for machine learning  

# How to use  
   1. get some videos  
   1. define labels as json  
      *  sample  

             { "videoAndLabels" : [ { "name" : "201801232200"
                                    , "status" : [ { "label" : "else"
                                                   , "until" : "00:00:00.500"
                                                   }
                                                 , { "label" : "N"
                                                   , "until" : "00:00:40.000"
                                                   }
                                                 , { "label" : "A"
                                                   , "until" : "00:02:40.000"
                                                   }
                                                 , { "label" : "B"
                                                   , "until" : "00:05:36.000"
                                                   }
                                                 , { "label" : "A"
                                                   , "until" : "00:12:10.000"
                                                   }
                                                 , { "label" : "B"
                                                   , "until" : "00:13:05.000"
                                                   }
                                                 , { "label" : "C"
                                                   , "until" : "inf"
                                                   }
                                                 ]
                                    }
                                  ]
             }

      *  json details
         +  *videoAndLabels*: package of this json  
         +  *name*: video name which you got  
         +  *status*:  
            -  *label*: label of choped pics  
            -  *until*: time mark of label  
               (`inf` means end of file beacuse this program made by python)  
   1. run `video_cutter.py`  

# TODO
   *  make size of cutting window more flexible  
   *  and so on

