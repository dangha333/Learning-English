importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.10/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyCg9wLWjLkwf5mCaRsAcp3obVi-CKXoH-E",
   authDomain: "learning-english-56f73.firebaseapp.com",
  projectId: "learning-english-56f73",
  messagingSenderId: "339132124762",
   appId: "1:339132124762:web:48a113f910f12fd84a1263",
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  self.registration.showNotification(payload.notification.title, {
    body: payload.notification.body,
    icon: '/icon-192.png'
  });
});
