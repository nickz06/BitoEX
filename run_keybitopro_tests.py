import pytest

if __name__ == '__main__':
    pytest.main([
        'tests/warranty/test_key_bitopro.py',
        '--html=reports/bitopro_report.html', '--self-contained-html',
        '--variables' , 'credentials.toml'
    ])


#tests/frontend/test_frontend_all_functions.py
