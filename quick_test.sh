#!/bin/bash
# Quick test command for WhatsApp Watcher

echo "=========================================="
echo "Testing WhatsApp Watcher - Quick Check"
echo "=========================================="
echo ""

cd "D:\LEEZA\HACKATHON 0\silver"

echo "Step 1: Checking if files exist..."
if [ -f "AI_Employee_Vault/whatsapp_watcher.py" ]; then
    echo "[OK] whatsapp_watcher.py found"
else
    echo "[ERROR] whatsapp_watcher.py not found!"
    exit 1
fi

echo ""
echo "Step 2: Running test script..."
python test_whatsapp_ai.py

echo ""
echo "=========================================="
echo "Test Complete!"
echo "=========================================="
echo ""
echo "Check created files:"
ls -lh AI_Employee_Vault/Needs_Action/whatsapp_*.md
echo ""
echo "To test with real WhatsApp:"
echo "  1. Run: START_WHATSAPP_WITH_AI.bat"
echo "  2. Scan QR code"
echo "  3. Send test message from phone"
echo ""
