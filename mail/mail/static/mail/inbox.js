document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

  document.querySelector('#compose-form').onsubmit = function() {
    const subject = document.querySelector('#compose-subject').value;
    const recipients = document.querySelector('#compose-recipients').value;
    const body = document.querySelector('#compose-body').value;
    fetch('/emails', {
      method:'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log(result);
        })
    .catch(error => {
      console.log('Error:', error);
      });
      load_mailbox('sent');
      return false
    }
  });
  
  
function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
};


function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  if (mailbox === 'archive') {
    fetch('/emails/archive')
    .then(response => response.json())
    .then(emails => {
    console.log(emails);
    })
  }

  if (mailbox === 'inbox') {
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
      for (let i = 0; i < emails.length; i++) {
        const subject = emails[i].subject;
        const sender = emails[i].sender;
        const timestamp = emails[i].timestamp;
        const read = emails[i].read;
        const id = emails[i].id;
        const element = document.createElement('div');
        element.id = id
        element.innerHTML = `${timestamp} Subject: ${subject}. From: ${sender}`
        if (read) {
          element.style.backgroundColor = 'lightgray';
        }
        const emailsview = document.querySelector('#emails-view')
        emailsview.append(element);
        
        element.addEventListener('click', function() {
          fetch(`/emails/${element.id}`)
          .then(response => response.json())
          .then(email => {
            //PUT REQUEST FOR READ
            console.log(email.read)
            const subject = email.subject
            const sender = email.sender
            const timestamp = email.timestamp
            const body = email.body
            element.style.backgroundColor = 'white'

          })
        }
      )}
  });
  }
  //{
    //"id": 100,
    //"sender": "foo@example.com",
    //"recipients": ["bar@example.com"],
    //"subject": "Hello!",
    //"body": "Hello, world!",
    //"timestamp": "Jan 2 2020, 12:00 AM",
    //"read": false,
    //"archived": false
//}

  if (mailbox === 'sent') {
    fetch('/emails/sent')
    .then(response => response.json())
    .then(emails => {
    console.log(emails);
    })
  }
};