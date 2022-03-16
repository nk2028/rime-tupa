# rime-tshet

rime 切韻拼音輸入方案

[切韻拼音](https://zhuanlan.zhihu.com/p/478751152)（Tshet-uinh Phonetic Alphabet，可簡稱切拼或 TUPA）是爲切韻音系創制的拼音方案，用於拼寫與切韻音系相合的南北朝中期到隋初中古漢語。

本輸入方案旨在爲 rime 輸入法增加切韻拼音輸入支援，使得用戶可以簡便地利用切韻拼音輸入中文字，是學習漢語音韻學的有效工具。除本切韻拼音輸入方案外，用戶還可以利用[切韻音系自動推導器](https://nk2028.shn.hk/qieyun-autoderiver/)與[韻鑒 APP](https://zhuanlan.zhihu.com/p/361127660) 查詢漢字的切韻拼音。

## 功能

1\. 直接輸入切韻拼音

![](demo/1.png)

2\. 聲母簡拼

![](demo/2.png)

3\. 普通話反查切韻（先按 <kbd>`</kbd>，再輸入普通話）

![](demo/3.png)

4\. 粵語反查切韻（先按 <kbd>f</kbd>，再輸入粵語）

![](demo/4.png)

※ 註：反查功能尚不完善，某些詞語無法顯示讀音。

## 安裝

### Windows 安裝方法

**第一步：安裝小狼毫前臺程式**

※ 註：如果你之前已經安裝過小狼毫，請轉至第二步。

從 rime 官方網站 <https://rime.im/> 下載並安裝小狼毫輸入法。

**第二步：下載切韻拼音**

用 WinKey + <kbd>Space</kbd> 切換至小狼毫輸入法。

右擊「中」，點選「輸入法設定」。

![](https://camo.githubusercontent.com/aabb02dd5cd3dc8fbbff33efd6201707ad0fad94cb1e6ce913ce36684c619325/68747470733a2f2f692e696d6775722e636f6d2f5858484d5343432e706e67)

點擊「獲取更多輸入方案...」。

![](https://camo.githubusercontent.com/97f42eb9aff6a44934777e2568ff5e6dc7a648266bbdc01739ec09d5810d718e/68747470733a2f2f692e696d6775722e636f6d2f657578684543562e706e67)

在跳出的視窗中鍵入 `cantonese` 以安裝粵語輸入方案（用於反查），按下 <kbd>Enter</kbd>。然後鍵入 `ayaka14732/rime-tshet`，按下 <kbd>Enter</kbd>。

![](https://camo.githubusercontent.com/9609be7beef59bc18bb006aa95c8d17238f2ad45e0f88a274bc03d3984bad1c1/68747470733a2f2f692e696d6775722e636f6d2f315871617959382e706e67)

**第三步：選取輸入法**

關閉跳出的視窗，返回「輸入法設定」，勾選「切韻拼音」，然後點擊「中」。

然後選擇符合自己喜好的佈景主題，再點擊「中」完成設定。

![](https://camo.githubusercontent.com/59daa1cbd01f2a9ca20674be4f2cdaad02a047cfa31c69e213caa278e8c2b222/68747470733a2f2f692e696d6775722e636f6d2f354e6d476247332e706e67)

回到選單點擊「重新部署」，等待程式處理詞庫資料。

![](https://camo.githubusercontent.com/d0d5806ce3cafbb50f3dfcf363163b9a67f2e2b1432e437f59e6ab57fd5298c5/68747470733a2f2f692e696d6775722e636f6d2f7a6b507964624c2e706e67)

然後按下 <kbd>F4</kbd>（或者 <kbd>Ctrl</kbd> 加 <kbd>`</kbd>，注意是數字 1 左邊的按鍵，並非單引號！），就可以看到「切韻拼音」了（你可能要按下 <kbd>=</kbd> 翻頁纔可以找到）。

### macOS 安裝方法

**第一步：安裝鼠須管前臺程式**

※ 註：如果你之前已經安裝過鼠須管，請轉至第二步。

從 rime 官方網站 <https://rime.im/> 下載並安裝鼠須管輸入法。

**第二步：下載切韻拼音**

打開 Terminal，複製粘貼以下命令：

```sh
curl -fsSL https://git.io/rime-install | bash -s -- cantonese ayaka14732/rime-tshet custom:set:config=default,key=installed_from,value=ayaka14732/rime-tshet custom:clear_schema_list custom:add:schema=tshet custom:add:schema=luna_pinyin custom:add:schema=jyut6ping3
```

在命令執行過程中，可能會跳出視窗提示安裝 git，要點選允許，否則無法正常安裝。

註：[怎樣打開 Terminal？](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)

（或使用 <kbd>Ctrl</kbd> + <kbd>Enter</kbd>，用 Spotlight 搜尋並開啓 terminal）

**第三步：選取輸入法**

依次點按以下兩個按鈕：

![](https://camo.githubusercontent.com/d95f9084049b7f97711737fcaaa3cc82411764da5bb6da3bb1313d5742075a64/68747470733a2f2f692e696d6775722e636f6d2f366139435331522e6a7067)

然後按下 <kbd>Ctrl</kbd> 加 <kbd>`</kbd>（注意是數字 1 左邊的按鍵，並非單引號！），就可以看到「切韻拼音」了（你可能要按下 <kbd>=</kbd> 翻頁纔可以找到）。

**可選步驟：自定義外觀**

將[此配置檔](https://gist.githubusercontent.com/laubonghaudoi/40f4ad4036a321a21fb2f32229892f55/raw/958e050a57cc3da7abe0ba16510d61e95ad2b9ee/squirrel.custom.yaml)保存在「rime 用戶文件夾」中，重新部署，就可以見到外觀變化了。

### Arch Linux 安裝方法

**第一步：安裝 Fcitx5 輸入法程式**

※ 註：詳見 [Fcitx5 - ArchWiki](https://wiki.archlinux.org/index.php/Fcitx5)。

```sh
sudo pacman -S fcitx5 fcitx5-qt fcitx5-gtk fcitx5-rime kcm-fcitx5
```

編輯 `/etc/environment`，加入：

```sh
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
```

然後重新登入。

（你可能需要手動啓動 Fcitx5 程式）

開啓 Fcitx5 設定，啓用 rime。

**第二步：安裝切韻拼音**

從 AUR 安裝 [`rime-tshet`](https://aur.archlinux.org/packages/rime-tshet)。

```sh
yay -S rime-tshet
```

新建 `~/.local/share/fcitx5/rime/default.custom.yaml`：

```yaml
patch:
  schema_list:
    - schema: tshet
```

然後重新部署。

**可選步驟：自定義外觀**

可以使用 [hosxy/Fcitx5-Material-Color](https://github.com/hosxy/Fcitx5-Material-Color) 等佈景主題。

### FreeBSD 安裝方法

**第一步：安裝 Fcitx5 輸入法程式**

```sh
pkg install fcitx5 fcitx5-configtool fcitx5-gtk fcitx5-qt zh-fcitx5-rime zh-rime-essay
```

安裝時會提示執行以下命令：

```sh
cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
```

新建 `~/.xprofile`：

```sh
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

重新啓動系統後，在輸入法圖標上點按右鍵，開啓 Fcitx5 配置，然後添加 rime。

**第二步：安裝切韻拼音**

由於 pkg 並未包含切韻拼音，需要手動安裝。

```sh
mkdir -p ~/.local/share/fcitx5/rime/opencc
git clone https://github.com/ayaka14732/rime-tshet.git ~/.rime-tshet
ln -s ~/.rime-tshet/*.yaml ~/.local/share/fcitx5/rime
git clone https://github.com/rime/rime-cantonese.git ~/.rime-cantonese
ln -s ~/.rime-cantonese/*.yaml ~/.local/share/fcitx5/rime
ln -s ~/.rime-cantonese/opencc/* ~/.local/share/fcitx5/rime/opencc
```

新建 `~/.local/share/fcitx5/rime/default.custom.yaml`：

```yaml
patch:
  schema_list:
    - schema: tshet
```

然後重新部署。

**可選步驟：自定義外觀**

可以使用 [hosxy/Fcitx5-Material-Color](https://github.com/hosxy/Fcitx5-Material-Color) 等佈景主題。

**卸載方法**

卸載切韻拼音：

```sh
rm -rf ~/.rime-tshet
rm -rf ~/.rime-cantonese
find -L ~/.local/share/fcitx5/rime -maxdepth 1 -type l -exec rm -- {} +
find -L ~/.local/share/fcitx5/rime/opencc -maxdepth 1 -type l -exec rm -- {} +
rm -f ~/.local/share/fcitx5/rime/default.custom.yaml
```

卸載 Fcitx5 輸入法程式：

```sh
pkg remove fcitx5 fcitx5-configtool fcitx5-gtk fcitx5-qt zh-fcitx5-rime zh-rime-essay
rm -f ~/.xprofile
```

## 開發

本倉庫資料來源爲 [ayaka14732/rime-kyonh](https://github.com/ayaka14732/rime-kyonh)。

構建方法：

```sh
npm install
rm -rf cache *.dict.yaml
mkdir -p cache
node scripts/generate_map.js
python scripts/build.py
python scripts/build_unspaced.py
python scripts/uniqsort.py
```
