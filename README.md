MLTools_PyQt4
==

```
用于批量处理，标记训练样本的工具
```

> Dependence

```
基础依赖：
	PyQt4
	numpy
	python-opencv
可选依赖：
	matlab 	使用2维混合高斯模型标记人体区域图形 modular_matlab
	h5py	查看hdf5数据库图像工具 DataSet_Viewer
```

> 目录

```
Core/								#核心模块，主要包含一些图像处理相关的包和工具
  |-> DocManager/ 					#基于python的文件管理包
  |-> modular_c/					#基于c/c++编写的模块	
        |-> linux_DirectoryBrowser/	#基于linux_c的文件管理包
  |-> modular_matlab/				#基于matlab的工具
        |-> guassian_body_model/ 	#2维混合高斯模型人体区域图形标记工具
  |-> pyte/							#基于PyQt4的伪终端窗口对象
Tools/								#工具包
  |-> DataSet_Viewer/				#查看hdf5数据库图像工具
  |-> DocManagerTool/				#文件管理工具，方便过滤，基于DocManager包
  |-> pyqtterm/ 					#基于PyQt4的伪终端窗口对象,可以嵌入qt程序
  |-> SampleTool_m/					#新版的样本处理工具，基于PyQt4
  |-> ShellManagerTool/				#linux shell管理工具
```
