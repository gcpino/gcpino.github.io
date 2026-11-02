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
    
    # 3. Check colors (Slate 900)
    assert '--bg: #0f172a;' in content, "Background color variable not updated to Slate 900"
    assert '--bg-card: #1e293b;' in content, "Card background variable not updated"
    assert '--border: #334155;' in content, "Border variable not updated"
    assert '--accent: #649ad2;' in content, "Accent color not updated to site blue"
    assert "rgba(15, 23, 42" in content, "Navbar or Matrix canvas RGB clear color not updated to slate-900"
    
    # 4. Check old template projects removal
    assert "<h4>forge</h4>" not in content, "forge project header still exists"
    assert "details-forge" not in content, "forge project details still exists"
    assert "<h4>bedrock</h4>" not in content, "bedrock project header still exists"
    assert "details-bedrock" not in content, "bedrock project details still exists"
    assert "<h4>vault</h4>" not in content, "vault project header still exists"
    assert "details-vault" not in content, "vault project details still exists"
    assert "<h4>synapse</h4>" not in content, "synapse project header still exists"
    assert "details-synapse" not in content, "synapse project details still exists"
    assert "<h4>ember</h4>" not in content, "ember project header still exists"
    assert "details-ember" not in content, "ember project details still exists"
    assert "<h4>cachet</h4>" not in content, "cachet project header still exists"
    assert "details-cachet" not in content, "cachet project details still exists"
    assert "<h4>trace</h4>" not in content, "trace project header still exists"
    assert "details-trace" not in content, "trace project details still exists"
    
    # 5. Check all 7 projects and their GitHub links are present
    expected_projects = [
        ("balloc", "https://github.com/gcpino/balloc", "proj-balloc"),
        ("aes256", "https://github.com/gcpino/aes256", "proj-aes256"),
        ("SentinelMesh", "https://github.com/gcpino/SentinelMesh", "proj-sentinelmesh"),
        ("sdr", "https://github.com/gcpino/sdr", "proj-sdr"),
        ("c-infer", "https://github.com/gcpino/c-infer", "proj-cinfer"),
        ("PINN", "https://github.com/gcpino/PINN", "proj-pinn"),
        ("spsc", "https://github.com/gcpino/spsc", "proj-spsc"),
    ]
    for name, url, anchor in expected_projects:
        assert name in content, f"{name} project not found"
        assert url in content, f"{name} GitHub link ({url}) not found"
        assert f'id="{anchor}"' in content, f"Card anchor id={anchor} not found"

    # 6. Check project categories, minimal filter bar, and collapsible output toggles
    assert ">Systems &amp; Memory<" in content, "Systems & Memory category not found"
    assert ">Cryptography<" in content, "Cryptography category not found"
    assert ">Mesh Networking<" in content, "Mesh Networking category not found"
    assert ">Signal Processing<" in content, "Signal Processing category not found"
    assert ">Machine Learning<" in content, "Machine Learning category not found"
    assert ">Physics<" in content, "Physics category not found"
    assert ">Concurrency<" in content, "Concurrency category not found"
    assert 'class="filter-bar"' in content, "Minimal category filter bar missing"
    assert 'class="out-toggle"' in content, "Collapsible output toggle missing"
    
    # 7. Check minimalist layout (no heavy sidebar, shader canvas, or telemetry panel clutter)
    assert 'id="doc-sidebar"' not in content, "Heavy fixed sidebar still present"
    assert 'id="shader-canvas"' not in content, "Old shader canvas still present"
    assert 'class="sys-panel"' not in content, "Cluttered hero telemetry panel still present"
    assert "matrix-canvas" not in content, "Matrix rain canvas still present"
    assert "Matrix Rain" not in content, "Matrix rain JS still present"

    # 8. Check LinkedIn handle is gcorpas
    assert 'linkedin.com/in/gcorpas' in content, "LinkedIn handle not updated to gcorpas"

    print("All portfolio tests PASSED successfully!")

if __name__ == "__main__":
    test_portfolio()
