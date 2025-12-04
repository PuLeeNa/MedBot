// Backend API URL
const API_URL = 'https://medbot-jvsz.onrender.com';

// Hide loading overlay when page is fully loaded
window.addEventListener('load', function() {
    setTimeout(function() {
        document.getElementById('loading-overlay').style.display = 'none';
    }, 1000);
});

$(document).ready(function() {
    const botLogoUrl = "logo.jpg";
    
    $("#messageArea").on("submit", function(event) {
        event.preventDefault();
        
        const date = new Date();
        const hour = date.getHours();
        const minute = date.getMinutes();
        const str_time = hour + ":" + minute;
        const rawText = $("#text").val();

        const userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + rawText + '<span class="msg_time_send">'+ str_time + '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
        
        $("#text").val("");
        $("#messageFormeight").append(userHtml);
        
        // Show typing indicator
        const typingHtml = '<div class="d-flex justify-content-start mb-4" id="typingIndicator"><div class="img_cont_msg"><img src="' + botLogoUrl + '" class="rounded-circle user_img_msg"></div><div class="msg_cotainer"><div class="typing-indicator"><span></span><span></span><span></span></div></div></div>';
        $("#messageFormeight").append(typingHtml);
        
        // Scroll to bottom
        $("#messageFormeight").scrollTop($("#messageFormeight")[0].scrollHeight);

        // Make API call
        $.ajax({
            url: API_URL + "/get",
            type: "POST",
            data: { msg: rawText },
            success: function(data) {
                $("#typingIndicator").remove();
                const botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="' + botLogoUrl + '" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + data + '<span class="msg_time">' + str_time + '</span></div></div>';
                $("#messageFormeight").append($.parseHTML(botHtml));
                $("#messageFormeight").scrollTop($("#messageFormeight")[0].scrollHeight);
            },
            error: function() {
                $("#typingIndicator").remove();
                const errorHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="' + botLogoUrl + '" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">Sorry, I encountered an error. Please try again.<span class="msg_time">' + str_time + '</span></div></div>';
                $("#messageFormeight").append($.parseHTML(errorHtml));
                $("#messageFormeight").scrollTop($("#messageFormeight")[0].scrollHeight);
            }
        });
    });
});
