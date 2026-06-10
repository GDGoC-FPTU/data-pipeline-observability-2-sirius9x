[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24112884&assignment_repo_type=AssignmentRepo)

# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** thachdoanxuan@gmail.com
**Name:** Doan Xuan Thach

---

## Mo ta

Bai lab xay dung mot ETL pipeline tu dong bang Python va pandas. Pipeline doc du
lieu san pham tu JSON, loai cac record co gia khong hop le hoac category rong,
chuan hoa category thanh Title Case, tinh gia giam 10%, them timestamp xu ly va
luu ket qua ra CSV.

Bai lam cung co mot Stress Test de so sanh phan hoi cua Agent khi su dung du lieu
sach va du lieu rac. Ket qua cho thay outlier va cac loi chat luong du lieu co
the lam Agent dua ra cau tra loi sai lech.

---

## Cach chay

### Cai dat

```bash
pip install pandas pytest
```

### Chay ETL Pipeline

```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)

1. Chay ETL Pipeline de tao file du lieu sach `processed_data.csv`:

```bash
python solution.py
```

2. Tao file `garbage_data.csv` chua cac loi chat luong du lieu nhu duplicate ID,
price sai kieu, outlier va gia tri null:

```bash
python generate_garbage.py
```

3. Chay Agent voi cung mot cau hoi tren ca du lieu sach va du lieu rac:

```bash
python agent_simulation.py
```

Agent se doc `processed_data.csv` truoc, sau do doc `garbage_data.csv` va chon
san pham electronics co gia cao nhat trong tung bo du lieu.

Ket qua du kien:

```text
Testing with CLEAN data:
Agent: Based on my data, the best choice is Laptop at $1200.

Testing with GARBAGE data:
Agent: Based on my data, the best choice is Nuclear Reactor at $999999.
```

Ket qua cho thay outlier trong du lieu rac co the chi phoi logic tim kiem va lam
Agent dua ra cau tra loi khong hop ly. Phan so sanh va phan tich chi tiet duoc ghi
trong `experiment_report.md`.

### Chay test

```bash
python -m pytest -v
```

---

## Cau truc thu muc

```text
solution.py             # ETL pipeline
raw_data.json           # Du lieu dau vao
processed_data.csv      # Du lieu sach sau ETL
generate_garbage.py     # Tao du lieu rac
garbage_data.csv        # Du lieu dung cho Stress Test
agent_simulation.py     # Mo phong Agent
experiment_report.md    # Bao cao ket qua thi nghiem
tests/                  # Cac bai test tu dong
```

---

## Ket qua

- Pipeline doc 5 record tu `raw_data.json`.
- 3 record hop le duoc giu lai va 2 record khong hop le bi loai.
- Clean Data: Agent chon Laptop voi gia $1200.
- Garbage Data: Agent bi outlier chi phoi va chon Nuclear Reactor voi gia
  $999999.
- Ket qua chi tiet va phan tich duoc ghi trong `experiment_report.md`.
