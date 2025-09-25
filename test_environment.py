#!/usr/bin/env python3
"""
Test script to verify the economic analysis environment is working correctly
"""

import sys
import importlib

def test_import(package_name, display_name=None):
    """Test if a package can be imported"""
    display_name = display_name or package_name
    try:
        importlib.import_module(package_name)
        print(f"✅ {display_name}: OK")
        return True
    except ImportError as e:
        print(f"❌ {display_name}: FAILED - {e}")
        return False

def main():
    print("🧪 Testing Economic Analysis Environment")
    print("=" * 50)
    
    # Test Python version
    version = sys.version_info
    if (version.major, version.minor) >= (3, 9):
        print(f"✅ Python: OK (Version {version.major}.{version.minor}.{version.micro})")
    else:
        print(f"❌ Python: Version too old")
        return False
    
    # Test core packages
    packages_to_test = [
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('jupyter', 'Jupyter'),
        ('wbdata', 'World Bank Data'),
        ('plotly', 'Plotly')
    ]
    
    results = []
    for package, name in packages_to_test:
        results.append(test_import(package, name))
    
    # Test our custom modules
    try:
        from src.data.world_bank_collector import WorldBankDataCollector
        print("✅ Custom modules: OK")
        results.append(True)
    except ImportError as e:
        print(f"❌ Custom modules: FAILED - {e}")
        results.append(False)
    
    print("=" * 50)
    
    if all(results):
        print("🎉 All tests passed! Environment is ready.")
        print("\n🚀 Next steps:")
        print("1. Run: jupyter lab")
        print("2. Open notebooks/01_data_collection/economic_data_demo.ipynb")
        print("3. Start your economic analysis!")
        return True
    else:
        print("⚠️  Some tests failed. Please check your environment.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
