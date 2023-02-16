import pytest

if __name__ == '__main__':
    pytest.main([
        'tests/warranty/test_bitopro_vip.py',
        '--html=reports/bitopro_vip_report.html', '--self-contained-html',
        '--variables' , 'credentials.toml'
    ])


#tests/frontend/test_frontend_all_functions.py
