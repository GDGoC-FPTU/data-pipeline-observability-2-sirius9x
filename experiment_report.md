# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-XXXX
**Name:** (Dien ten cua ban)
**Date:** 2026-06-10

---

## 1. Ket qua thi nghiem

Da chay `agent_simulation.py` voi cung truy van:
`What is the best electronic product?`

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200. | 9/10 | Agent doc dung du lieu da qua validation va chon san pham electronics co gia cao nhat. |
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999. | 1/10 | Gia outlier rat lon lam ket qua bi sai lech va khong con phu hop voi nhu cau mua sam thong thuong. |

---

## 2. Phan tich va nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Agent chon san pham co gia cao nhat trong category electronics ma khong kiem tra
tinh hop ly cua gia. Trong bo Garbage Data, Nuclear Reactor co gia 999999, la mot
outlier rat lon, nen no lap tuc vuot qua Laptop va tro thanh ket qua duoc chon.
Day la nguyen nhan truc tiep lam cau tra loi sai lech.

Ngoai ra, duplicate ID co the lam Agent nham lan danh tinh record; price dang chu
nhu "ten dollars" co the gay loi khi sap xep hoac tinh toan; null ID va category
lam mat ngu canh; record gia bang 0 cung la du lieu khong hop le. Neu khong co
validation, cac loi nay co the lam Agent tra loi sai, bo sot san pham, hoac dung
hoan toan. Ket qua cho thay chat luong dau vao anh huong truc tiep den do tin cay
cua cau tra loi, du logic truy van khong thay doi.

---

## 3. Ket luan

**Quality Data > Quality Prompt?**

Dong y. Prompt tot chi huong dan Agent cach tim cau tra loi, nhung khong the sua
duoc outlier, sai kieu, duplicate hay gia tri null trong nguon du lieu. Can
validate va theo doi chat luong du lieu truoc khi dua vao Agent.
