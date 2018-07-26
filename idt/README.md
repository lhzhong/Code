## 视频IDT特征的提取

> idt特征源码下载：[wangheng](http://lear.inrialpes.fr/people/wang/dense_trajectories)

### 使用步骤：

**1.安装opencv**

> 参考 [opencv安装](https://github.com/lhzhong/iNote/blob/master/Install_Caffe(GPU).md)

**2.安装ffmpeg**
> 参考 [ffmpeg安装](https://github.com/lhzhong/iNote/blob/master/Install_ffmpeg.md)

**3.编译（进入idt目录）**
```
make
```

**4.单视频测试**
```
./release/Video ./test_sequences/person01_boxing_d1_uncomp.avi
```

**5.IDT特征的提取**
```
./release/DenseTrackStab ./test_sequences/person01_boxing_d1_uncomp.avi
```
若要提取特征为文本形式
```
./release/DenseTrackStab ./test_sequences/person01_boxing_d1_uncomp.avi | gzip > out.features.gz
```

**6.批量视频特征提取**

在matlab下运行`extractIDT.m`文件

