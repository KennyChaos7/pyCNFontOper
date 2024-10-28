# 接口文档





## 接口的调用顺序

### 首先需要先进行**两次上传图片操作，服务器计算需要**，然后再发送**要进行对比的两个图片的filename**，服务器计算重合率后返回

### 如果需要染色处理后的图片，则需要先进行**一次图片上传图片操作**，然后调用**op_unwrap_n_replace图片染色**，最后根据返回**filepath参数，在服务器上的缓存图片路径**

## 接口列表

| 接口名称                                               | 入参                                                         | 返回                                                         |            | 接口说明                           |
| ------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---------------------------------- |
| /upload_img                                            | 文件（png格式）                                              | {<br/>    "filename": "20240818205011.png",<br/>    "filepath": "static/png/20240818205011.png"<br/>} | 返回json   | 上传图片                           |
| /op_unwrap_n_replace?filename=                         | GET （filename为**上传图片后返回的filename**）               | {<br/>    "filename": "20240818204749.png",<br/>    "filepath": "static/png/20240818204749.png"<br/>} | 返回json   | 图片染色                           |
| /op_unwrap_n_replace_2?filename=                       | GET（filename为**上传图片后返回的filename**）                |                                                              | 返回文件   | 图片染色                           |
| /compare_img?filename1=&filename2=                     | GET（filename为**上传图片后返回的filename**）                | {'ssim': 0.00}                                               | 返回重合率 | 将两张已经上传过图片进行重合率计算 |
| /op_unwrap_color_replace?filename=&red=&green=&blue=   | GET（filename为**上传图片后返回的filename**, **red**，**green**, **blue**分别**int**的纯数字颜色色值） | {<br/>    "filename": "20240818204749.png",<br/>    "filepath": "static/png/20240818204749.png"<br/>} | 返回json   | 图片自定义颜色染色                 |
| /op_unwrap_color_replace_2?filename=&red=&green=&blue= | GET（filename为**上传图片后返回的filename**, **red**，**green**, **blue**分别**int**的纯数字颜色色值）） |                                                              | 返回文件   | 图片自定义颜色染色                 |
| /remove_img_cache?filename=                            | GET（filename为**上传图片后返回的filename**）                |                                                              |            | 删除对应图片缓存                   |
| /remove_all_img_cache?                                 | GET                                                          |                                                              |            | 删除全部图片缓存                   |

