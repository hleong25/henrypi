# henrypi-api

# mjpeg-streamer

https://github.com/jacksonliam/mjpg-streamer

```
/usr/local/bin/mjpg_streamer -i "input_uvc.so --device /dev/video0 -f 100 -r 1280x960" -o "output_http.so -w /usr/local/share/mjpg-streamer/www"
```

https://www.acmesystems.it/video_streaming

# webcam info

```
# install utils
apt install v4l-utils

# get video devices
v4l2-ctl --list-devices

# get vidcap formats
-- find MJPG, then get index
root@2e48e576edfb:/code# v4l2-ctl -d /dev/video0 --list-formats
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'MJPG' (Motion-JPEG, compressed)
	[1]: 'YUYV' (YUYV 4:2:2)


# get framesizes
root@2e48e576edfb:/code# v4l2-ctl -d /dev/video0 --list-framesizes 0
ioctl: VIDIOC_ENUM_FRAMESIZES
	Size: Discrete 1280x720
	Size: Discrete 960x540
	Size: Discrete 848x480



```

```
Video Capture Formats options:
  --list-formats     display supported video formats [VIDIOC_ENUM_FMT]
  --list-formats-ext display supported video formats including frame sizes
                     and intervals
  --list-framesizes <f>
                     list supported framesizes for pixelformat <f>
                     [VIDIOC_ENUM_FRAMESIZES]
                     pixelformat is the fourcc value as a string
  --list-frameintervals width=<w>,height=<h>,pixelformat=<f>
                     list supported frame intervals for pixelformat <f> and
                     the given width and height [VIDIOC_ENUM_FRAMEINTERVALS]
                     pixelformat is the fourcc value as a string
  --list-fields      list supported fields for the current format
  -V, --get-fmt-video
     		     query the video capture format [VIDIOC_G_FMT]
  -v, --set-fmt-video
  --try-fmt-video width=<w>,height=<h>,pixelformat=<pf>,field=<f>,colorspace=<c>,
                  xfer=<xf>,ycbcr=<y>,hsv=<hsv>,quantization=<q>,
                  premul-alpha,bytesperline=<bpl>,sizeimage=<sz>
                     set/try the video capture format [VIDIOC_S/TRY_FMT]
                     pixelformat is either the format index as reported by
                       --list-formats, or the fourcc value as a string.
                     The bytesperline and sizeimage options can be used multiple times,
                       once for each plane.
                     premul-alpha sets V4L2_PIX_FMT_FLAG_PREMUL_ALPHA.
                     <f> can be one of the following field layouts:
                       any, none, top, bottom, interlaced, seq_tb, seq_bt,
                       alternate, interlaced_tb, interlaced_bt
                     <c> can be one of the following colorspaces:
                       smpte170m, smpte240m, rec709, 470m, 470bg, jpeg, srgb,
                       oprgb, bt2020, dcip3
                     <xf> can be one of the following transfer functions:
                       default, 709, srgb, oprgb, smpte240m, smpte2084, dcip3, none
                     <y> can be one of the following Y'CbCr encodings:
                       default, 601, 709, xv601, xv709, bt2020, bt2020c, smpte240m
                     <hsv> can be one of the following HSV encodings:
                       default, 180, 256
                     <q> can be one of the following quantization methods:
                       default, full-range, lim-range
```