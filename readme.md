
# 🧠 Weka 探索性與比較性分析完整教學

本文件為大數據課程期中考前複習筆記，內容涵蓋三大實作主題：分群、異常偵測、關聯規則探勘，搭配 Weka 工具與範例資料進行說明。

---

## 🔧 一、Weka 安裝與設定

### 1. Weka 安裝
- 前往下載頁：[https://waikato.github.io/weka-wiki/downloading_weka/](https://waikato.github.io/weka-wiki/downloading_weka/)
- 選擇含 Java VM 版本（64-bit 建議）
- 安裝方式：選擇 **Full** 安裝

### 2. 安裝套件
開啟 Weka → Tools → Package Manager，安裝以下套件：
- `cascadeKMeans`（分群）
- `localOutlierFactor`（異常偵測）
- `hotSpot`（關聯規則探勘）
- 自製套件：`WekaODF`（匯入 `.ods` 試算表）

### 3. 支援中文顯示（Windows）
修改 `RunWeka.ini`：
```ini
fileEncoding=utf-8
```

---

## 📁 二、準備資料
使用檔案：`stu-sch-1 - train.ods`  
來源：葡萄牙兩間學校，共 649 筆資料，30~33 欄位。

---

## 📊 三、探索性分析：分群（Clustering）

### ✅ 演算法
- 使用 `CascadeSimpleKMeans`
- 評估指標：Calinski-Harabasz (CH) 指標

### 🧪 操作步驟
1. 開啟 `.ods` 檔案（需安裝 WekaODF 套件）
2. 前處理：
   - 將 `Class` 欄設為「No class」
   - 使用 `NominalToBinary` 篩選器 → transformAllValues 設為 True → Apply
3. 執行分群：
   - 使用 `AddCluster` → 設定為 `CascadeSimpleKMeans`
   - 可調整群數（minNumClusters, maxNumClusters）
4. 檢視結果：
   - 會新增 `cluster` 欄位
   - 儲存為 `.csv` 檔 → 使用分群分析器分析群體差異

---

## 🧯 四、探索性分析：異常偵測（Anomaly Detection）

### ✅ 演算法
- 使用 `LOF`（Local Outlier Factor）
- 評估標準：`LOF > 1` 可能異常，`>1.5` 高度可疑

### 🧪 操作步驟
1. 開啟相同檔案
2. 關閉目標屬性（Class 設為 No class）
3. 套用篩選器：
   - `LOF`（需安裝 `localOutlierFactor`）
   - 點 `Apply` → 多出一欄 `LOF`
4. 儲存為 `.ods` → 用 LibreOffice 開啟，啟用 AutoFilter 排序 `LOF` 欄位

---

## 🔍 五、比較性分析：關聯規則探勘（Association Rule Mining）

### ✅ 演算法
- 使用 `HotSpot`（PRIM 方法）
- 評估指標：
  - Support（支持度）
  - Confidence（信賴度）
  - Lift（提升度）

### 🧪 操作步驟
1. 開啟資料檔
2. 切換到 `Associate` 頁籤
3. 選擇 `HotSpot` → 進階設定如下：
   - `maxBranchingFactor = 30`
   - `maxRuleLength = 1`
   - `outputRules = True`
   - `target = last`、`targetIndex = first`（或 2）
4. 點 `Start` 執行 → 觀看規則清單與其 Lift/Confidence 分數

---

## 📌 小提醒
- 分群與異常偵測屬於「**探索性分析**」，不需目標屬性。
- 關聯規則探勘屬於「**比較性分析**」，**必須指定目標屬性**（如 School）。
- 實作過程務必安裝對應套件，否則無法使用該演算法。

---

✅ 準備好了嗎？打開 Weka，實作一次就記住啦！
