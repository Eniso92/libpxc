# Copyright 2015 Intel Corporation. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'libpxc',
      'type': 'static_library',
      'sources': [
        'include/pxc3dscan.h',
        'include/pxc3dseg.h',
        'include/pxcaddref.h',
        'include/pxcaudio.h',
        'include/pxcaudiosource.h',
        'include/pxcbase.h',
        'include/pxcblobconfiguration.h',
        'include/pxcblobdata.h',
        'include/pxcblobmodule.h',
        'include/pxccalibration.h',
        'include/pxccapture.h',
        'include/pxccapturemanager.h',
        'include/pxcdefs.h',
        'include/pxcemotion.h',
        'include/pxcenhancedphoto.h',
        'include/pxcenhancedvideo.h',
        'include/pxcfaceconfiguration.h',
        'include/pxcfacedata.h',
        'include/pxcfacemodule.h',
        'include/pxchandconfiguration.h',
        'include/pxchanddata.h',
        'include/pxchandmodule.h',
        'include/pxchumantrackingmodule.h',
        'include/pxcimage.h',
        'include/pxcmetadata.h',
        'include/pxcobjectrecognitionconfiguration.h',
        'include/pxcobjectrecognitiondata.h',
        'include/pxcobjectrecognitionmodule.h',
        'include/pxcpersontrackingconfiguration.h',
        'include/pxcpersontrackingdata.h',
        'include/pxcpersontrackingmodule.h',
        'include/pxcphoto.h',
        'include/pxcplatformcameracontrol.h',
        'include/pxcpowerstate.h',
        'include/pxcprojection.h',
        'include/pxcsceneperception.h',
        'include/pxcsensemanager.h',
        'include/pxcsession.h',
        'include/pxcspeechrecognition.h',
        'include/pxcspeechsynthesis.h',
        'include/pxcstatus.h',
        'include/pxcsyncpoint.h',
        'include/pxctouchlesscontroller.h',
        'include/pxctracker.h',
        'include/pxctrackerutils.h',
        'include/pxcversion.h',
        'include/pxcvideomodule.h',
        'include/service/pxcaudiosourceservice.h',
        'include/service/pxcloggingservice.h',
        'include/service/pxcpowerstateserviceclient.h',
        'include/service/pxcschedulerservice.h',
        'include/service/pxcserializableservice.h',
        'include/service/pxcsessionservice.h',
        'include/service/pxcsmartasyncimpl.h',
        'include/service/pxcsyncpointservice.h',
        'src/libpxc/libpxc.cpp',
      ],
      'include_dirs': [
        'include',
      ]
    }],
}
