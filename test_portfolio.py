import os
import re

def test_portfolio():
    html_path = "index.html"
    assert os.path.exists(html_path), "index.html does not exist"
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Check name is Guillermo
    assert "Guillermo: Systems & Projects" in content, "Title name not updated"
    assert 'content="Guillermo"' in content, "Author meta tag not updated"
    assert 'class="logo">Guillermo</a>' in content, "Logo name not updated"
    assert 'guillermo@portfolio: bash' in content, "Terminal title not updated"
    assert 'Guillermo Systems Terminal' in content, "Terminal welcome message not updated"
    assert 'Guillermo: Software Engineer' in content, "Terminal whoami not updated"
    
    # 2. Check no Spike remains
    assert "Spike" not in content, "Found remaining 'Spike' reference"
    assert "spike" not in content.lower(), "Found remaining 'spike' reference (lowercase/email)"
    
    # 3. Check colors (Slate 900 base tokens)
    assert '--bg: #0f172a;' in content, "Background color variable not updated to Slate 900"
    assert '--bg-card: #1e293b;' in content, "Card background variable not updated"
    assert '--border: #334155;' in content, "Border variable not updated"
    assert '--accent: #649ad2;' in content, "Accent color not updated to site blue"
    assert "rgba(15, 23, 42" in content, "Navbar clear color not updated to slate-900"
    
    # 4. Check old template projects removal
    old_projects = ["forge", "bedrock", "vault", "synapse", "ember", "cachet", "trace"]
    for old in old_projects:
        assert f"<h4>{old}</h4>" not in content, f"{old} project header still exists"
        assert f"details-{old}" not in content, f"{old} project details still exists"
    
    # 5. Check active featured projects: ONLY c-infer and PINN
    active_projects = [
        ("c-infer", "https://github.com/gcpino/c-infer", "proj-cinfer"),
        ("PINN", "https://github.com/gcpino/PINN", "proj-pinn"),
    ]
    for name, url, anchor in active_projects:
        assert name in content, f"{name} project not found"
        assert url in content, f"{name} GitHub link ({url}) not found"
        assert f'id="{anchor}"' in content, f"Card anchor id={anchor} not found"

    # 6. Check that the private repositories are NOT listed as project cards
    private_projects = ["balloc", "aes256", "SentinelMesh", "sdr", "spsc"]
    for priv in private_projects:
        assert f'id="proj-{priv.lower()}"' not in content, f"Private project {priv} card anchor still present"
        assert f'https://github.com/gcpino/{priv}' not in content, f"Private project {priv} link still present"

    # 7. Check modern aesthetic and architectural diagrams
    assert '<svg' in content, "Architecture SVG diagram missing"
    assert 'class="filter-bar"' in content, "Category filter bar missing"
    assert 'class="out-toggle"' in content, "Collapsible output toggle missing"
    assert 'assets/pinn-comparison.png' in content, "PINN comparison visualization missing"
    
    # 8. Check minimalist layout (no clutter)
    assert 'id="doc-sidebar"' not in content, "Heavy fixed sidebar still present"
    assert 'id="shader-canvas"' not in content, "Old shader canvas still present"
    assert 'class="sys-panel"' not in content, "Cluttered hero telemetry panel still present"
    assert "matrix-canvas" not in content, "Matrix rain canvas still present"

    # 9. Check LinkedIn handle is gcorpas
    assert 'linkedin.com/in/gcorpas' in content, "LinkedIn handle not updated to gcorpas"

    print("All portfolio tests PASSED successfully!")

if __name__ == "__main__":
    test_portfolio()
