import os
import re

def test_portfolio():
    html_path = "index.html"
    assert os.path.exists(html_path), "index.html does not exist"
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Check name is Guillermo
    assert "Guillermo — Systems & Projects" in content, "Title name not updated"
    assert 'content="Guillermo"' in content, "Author meta tag not updated"
    assert 'class="logo">Guillermo</a>' in content, "Logo name not updated"
    assert 'guillermo@portfolio — bash' in content, "Terminal title not updated"
    assert 'Guillermo Systems Terminal' in content, "Terminal welcome message not updated"
    assert 'Guillermo — Software Engineer' in content, "Terminal whoami not updated"
    
    # 2. Check no Spike remains
    assert "Spike" not in content, "Found remaining 'Spike' reference"
    assert "spike" not in content.lower(), "Found remaining 'spike' reference (lowercase/email)"
    
    # 3. Check colors (Slate 900)
    assert '--bg: #0f172a;' in content, "Background color variable not updated to Slate 900"
    assert '--bg-card: #1e293b;' in content, "Card background variable not updated"
    assert '--border: #334155;' in content, "Border variable not updated"
    assert '--accent: #3b82f6;' in content, "Accent color not updated to blue-500"
    assert "rgba(15, 23, 42" in content, "Navbar or Matrix canvas RGB clear color not updated to slate-900"
    
    # 5. Check projects removal
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
    
    # Check c-infer project is present
    assert "c-infer" in content, "c-infer project not found"

    # Check balloc project is present
    assert "balloc" in content, "balloc project not found"
    assert "https://github.com/gcpino/balloc" in content, "balloc GitHub link not found"

    # Check sdr project is present
    assert "sdr" in content, "sdr project not found"
    assert "https://github.com/gcpino/sdr" in content, "sdr GitHub link not found"

    # Check aes256 project is present
    assert "aes256" in content, "aes256 project not found"
    assert "https://github.com/gcpino/aes256" in content, "aes256 GitHub link not found"
    
    # 6. Check LinkedIn handle is gcorpas
    assert 'linkedin.com/in/gcorpas' in content, "LinkedIn handle not updated to gcorpas"

    print("All portfolio tests PASSED successfully!")

if __name__ == "__main__":
    test_portfolio()
