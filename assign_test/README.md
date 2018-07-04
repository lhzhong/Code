## Tensorflow: ValueError: GraphDef cannot be larger than 2GB.

Tensorflow的这个坑。。。

在做模型参数剪枝时，我跑了两个模型，LeNet-5和AlexNet，因为我的代码一开始是在LeNet-5上写的，所以当跑通LeNet-5网络时，我以为就大功告成了，
可是当我把代码移植到AlexNet网络时，我发现网络越跑越慢，我没太在意，让它自己跑着，可是当我过了一个晚上去查看结果时，
发现系统竟然报错```“ValueError: GraphDef cannot be larger than 2GB.”```
一开始我以为是我在把LeNet-5代码移植到AlexNet网络时，有些细节的东西搞错了，所以排错，确定无误后，继续跑，还是出现了这个问题。因此开始查具体原因。

然后我打开了模型文件，发现以前不在意的模型meta文件的内存竟然达到了快2G，而对比以前跑的网络的模型，这个meta文件只有几百k。
于是google，找原因，网上有把前向传播过程定义在sess.run()里的也出现这个问题，
因为我的实验写的比较冗杂，里面调用了不少模型保存、模型加载过程，所以我怀疑是不是不断的保存模型、加载模型导致最后模型大小剧增了，
因此不断进行优化代码，直到这个因素被排除，发现问题还是存在。

郁闷了很久。。。

一句句排错，后来终于发现了问题所在，由于剪枝后的权值要赋给原权值进行更新，
所以在tensorflow里有个assign函数就是干这事的，当我把assign函数去掉的时候，发现meta文件大小竟然不增加了，
究其原因，是因为tensorflow机制里，meta文件定义的是图结构，也就是运算图里的运算，
而我们在定义变量的时候，变量赋值的过程核心的其实也是通过这个assign操作进行的，
而每次的assign操作只会在图结构里增加运算，它不会进行覆盖，而我的输入数据又是比较大的，
所以每次的assign操作都会增加巨大的计算节点，最终导致模型爆炸。

查出了问题，下一步就是解决问题，具体的解决参考的
[stack overflow](https://stackoverflow.com/questions/42388563/tensorflow-graphdef-cannot-be-larger-than-2gb-error-when-saving-model-after/42906762)
里的一个类似问题

![icon](https://github.com/lhzhong/iNote/blob/master/pic/assign_problem.png)

他也是在sess.run()里进行了assign操作，怎么解决？

![icon](https://github.com/lhzhong/iNote/blob/master/pic/assign_solve.png)

把assign操作通过占位符的方式定义在sess.run()外，在sess.run()里只要输入数据即可。

通过这个骚操作，果然meta内存减小了，而且运算速度也变快了。

终于,从这个坑里跳出来了。。。

上面有v1 v2 v3三个代码

* v1是未优化的代码，也就是assign操作定义在sess.run()里的
* v2是经过优化的代码，通过占位符的方式输入数据
* v3与v2的差别是，因v2是在sess.run()里每次定义一个变量进行赋值，而v3是将多变量数组统一输入，这里的好处是，可能我每一次输入变量是不一样的，所以我需要提前先定义再输入

在我自己的代码中，占位符定义的特殊之处在于，因为我是针对权值变量进行定义，而网络每一层的权值shape不相同，所以需要取出每一层权值的shape进行定义，如下
![icon](https://github.com/lhzhong/iNote/blob/master/pic/assign_pruning.png)
