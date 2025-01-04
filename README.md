# AnimeRename
自用，一个纯靠AI🤖写的/非常简单的，适用于QBittorrent动画番剧自动重命名Python脚本，方便emby刮削

QB重命名工具更推荐使用[这位大佬的](https://github.com/Nriver/Episode-ReName)，但由于它好像不支持单集多版本（例如一集动画我喜欢下载多个字幕组的版本↓如图）

所以自己用AI 搓了一个...基本上是自用的，无任何编程基础，见谅捏

[推荐配合emby bangumi元数据插件食用，体验翻倍](https://github.com/kookxiang/jellyfin-plugin-bangumi)

![QQ截图20250105034556](https://github.com/user-attachments/assets/68c984da-15f6-411d-b22c-ca842af95015)
# 使用方法
[下载exe文件](https://github.com/ikemenrourou/AnimeRename/releases)
# 按照下面的设置
![QQ截图20250105025235](https://github.com/user-attachments/assets/7f0e4a31-63c6-42e2-8d80-bd77c5522fdc)
![QQ截图20250105025201](https://github.com/user-attachments/assets/05be9d1f-49f0-4221-a23b-c9f3abb5445a)
![QQ截图20250105025300](https://github.com/user-attachments/assets/aa737f6a-3843-4e9d-945d-8842c849e12a)



在Torrent完成时运行填写脚本路径（文件位置随意）
```
X:\你的文件夹\ReName.exe "%D" 15
```
---
在ReName.exe相同路径下创建一个prefixes.txt，可以实现替换/删除文字功能，源代码里有我自用现成的，你也可以自己创建

书写格式举例：
```
Up to 21°C，NC-Raws
Nekomoe kissaten，喵萌奶茶屋
3840x2160，4K
2.5次元的诱惑，次元的诱惑
2099，
```
注意中间有"，"符号

适用于面对作品里带数字的动画导致刮削错误或失败的情况

可以在prefixes.txt删除数字，简单粗暴的解决问题

例如<魔王2099>里的2099,<2.5次元的诱惑>里的2.5

