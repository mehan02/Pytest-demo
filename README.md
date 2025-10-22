# PyTest Demo – Calculator Unit Tests (with CI Integration)

A simple Python project demonstrating **PyTest** features — assertions, fixtures, parametrization, exception testing, mocking —  
plus **GitHub Actions CI** for automated testing and HTML reporting.

---

## Project Structure

 pytest-calculator-demo/
│
├── calculator.py 
├── test_calculator.py 
├── .github/
├── workflows/
└── pytest.yml 




---

## Local Setup

### Prerequisites
- Python 3.10+
- pip  
- pytest, pytest-html

### Install Dependencies
```bash
pip install pytest pytest-html
```

### Run Tests Locally
```bash
pytest -v
```

Generate HTML Report
```bash
pytest -v --html=report.html --self-contained-html
```

### References

- [PyTest Official Documentation](https://docs.pytest.org/)
- [PyTest Fixtures Guide](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [PyTest Mocking](https://docs.pytest.org/en/stable/how-to/mock.html)
- [GitHub Actions for Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

