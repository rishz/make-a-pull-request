import tensorflow as tf
from tensorflow import keras
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\HAIDER\\\\OneDrive\\\\Desktop\\\\prml\\\\project'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GPUs available = 0\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow import keras\n",
    "print(\"GPUs available = {}\".format(len(tf.config.experimental.list_physical_devices('GPU'))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Could not find a version that satisfies the requirement tf-nightly-gpu-2.0-preview (from versions: none)\n",
      "ERROR: No matching distribution found for tf-nightly-gpu-2.0-preview\n"
     ]
    }
   ],
   "source": [
    "!pip install tf-nightly-gpu-2.0-preview"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemError",
     "evalue": "gpu nahi mila",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mSystemError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-73c60334ac84>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mdevice_name\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgpu_device_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mdevice_name\u001b[0m\u001b[1;33m!=\u001b[0m\u001b[1;34m'/device:GPU:0'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mSystemError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'gpu nahi mila'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"GPU Mil gaya at : {}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdevice_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mSystemError\u001b[0m: gpu nahi mila"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "device_name = tf.test.gpu_device_name()\n",
    "if device_name!='/device:GPU:0':\n",
    "    raise SystemError('gpu nahi mila')\n",
    "print(\"GPU Mil gaya at : {}\".format(device_name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[name: \"/device:CPU:0\"\n",
      "device_type: \"CPU\"\n",
      "memory_limit: 268435456\n",
      "locality {\n",
      "}\n",
      "incarnation: 4680470337173576741\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "from tensorflow.python.client import device_lib\n",
    "print(device_lib.list_local_devices()) # list of DeviceAttributes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

print("GPUs available = {}".format(len(tf.config.experimental.list_physical_devices('GPU'))))
