## 视频光流特征的提取

### 使用步骤：

**1.安装opencv**

> 参考 [opencv安装](https://github.com/lhzhong/iNote/blob/master/Install_Caffe(GPU).md)

**2.打开CMakelist文件，将第5, 6行修改为：**
```
add_executable( Flow Flow.cpp )
target_link_libraries( Flow ${OpenCV_LIBS} )
```
> denseFlow改成自己的文件名称

**3.根目录问价夹下新建build和temp文件夹**

**4.编译（根目录文件下下执行）**
```
cmake .（cmake后有一空格）
make
```

**5.单视频特征提取**
```
./Flow -f test.avi -x tmp/flow_x -y tmp/flow_x -b 20
```

**6.批量视频特征提取**

在matlab下运行`extractOpticalFlow.m`文件

> 注意：光流特征提取有两种，一种是对视频分别生成x和y的光流图像，另一种是生成彩色光流图像。

#### 补充：flow文件夹下提取x和y的光流图像；flow_color文件夹下提取彩色光流。另外，rgb、gray、diff文件夹下分别提取帧图、灰度图和差分图
