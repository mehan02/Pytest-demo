
---

## 🕒 **Total = 6 minutes (3 presentation + 3 demo)**

---

### **A. Presentation (3 minutes)**

#### 1️⃣ Introduction & Context (≈45s)

* What PyTest is and why it exists
* Where it fits (unit, integration, functional testing)
* Why it matters (simplicity, automation, community)
* Brief mention of its industry adoption

✅ *Covers “Introduction & Context” rubric.*

---

#### 2️⃣ Features & Usage (≈1m15s)

**Slide:** Visual list or diagram

* Fixtures (setup/teardown)
* Parameterization
* Mocking
* CI Integration (GitHub Actions)
* Reporting (HTML)

**Slide:** “How it’s used” workflow

1. Write tests
2. Run `pytest`
3. Generate reports
4. Integrate with CI

✅ *Covers “Features & Usage” rubric.*

---

#### 3️⃣ Why It Stands Out (≈30s)

* Contrast briefly with older tools (e.g. unittest, nose)
* Mention plugin ecosystem (pytest-xdist, pytest-html)
* Optional: show statistic (adoption/downloads)

✅ *Adds extra insight for top-band marks.*

---

#### 4️⃣ Transition to Demo (≈30s)

* “Now we’ll show a quick working demo highlighting PyTest’s fixtures, parameterization, mocking, and CI reporting.”

✅ *Smooth transition for good structure & timing.*

---

### **B. Live Demo (3 minutes)**

#### 5️⃣ Code Walkthrough (≈1m)

* Show `calculator.py` (functions + class)
* Show `test_calculator.py` (fixture, parametrize, mock)
* Explain each section concisely (1 sentence each)

#### 6️⃣ Run the Tests (≈1m)

* Run: `pytest -v --html=report.html`
* Show terminal output (green check marks)
* Open `report.html` briefly to show generated report

#### 7️⃣ CI Integration (≈45s)

* Open `.github/workflows/pytest.yml`
* Explain automation: “Whenever code is pushed, GitHub Actions runs the tests and uploads an HTML report.”

#### 8️⃣ Summary & Wrap-Up (≈15s)

* “PyTest offers readable, powerful, and automated testing — ideal for modern software projects.”

✅ *Fully covers “Live Demo & Code” and “Presentation & Teamwork”.*

