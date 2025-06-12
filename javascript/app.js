document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const outputDiv = document.createElement("div");
    outputDiv.id = "orderSummary";
    outputDiv.className = "alert alert-info mt-4"; // Bootstrap class for styling

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent actual form submission

        form.after(outputDiv);

        const name = document.getElementById("InputFullName").value;
        const email = document.getElementById("EmailAddress").value;
        const product = document.getElementById("SelectProduct").value;
        const quantity = document.getElementById("Quantity").value;
        const paymentType = document.querySelector('input[name="PaymentType"]:checked');
        const paymentLabel = paymentType ? paymentType.parentElement.textContent.trim() : null;

        outputDiv.innerHTML = `
            <h4>Order Summary</h4>
            <p><strong>Name:</strong> ${name}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Product:</strong> ${product}</p>
            <p><strong>Quantity:</strong> ${quantity}</p>
            <p><strong>Payment Method:</strong> ${paymentLabel}</p>
        `;

        // Actually submit the form after showing summary
        setTimeout(() => {
            form.submit();
        }, 2000);

    });
});
