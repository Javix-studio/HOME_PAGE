function sendEmail() {
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
  
    // You can use any email sending service or API here
    // For example, using EmailJS:
    // emailjs.send('service_id', 'template_id', {email, message})
    //   .then((response) => {
    //     console.log('Email sent successfully!', response.status, response.text);
    //   })
    //   .catch((error) => {
    //     console.error('Failed to send email:', error);
    //   });
  
    // For simplicity, let's just log the email and message
    console.log('Email:', email);
    console.log('Message:', message);
  }