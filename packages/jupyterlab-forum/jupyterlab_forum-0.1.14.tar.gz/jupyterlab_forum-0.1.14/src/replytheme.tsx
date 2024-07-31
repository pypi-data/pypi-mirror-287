import { ShowThemeDetail } from './showthemedetail';

export async function handleReplyToTheme(widget: any, username: string, themeId: string, forumEndpointUrl: string) {
  // Temporary HTML for the reply form
  const replyFormHTML = `
    <h2>Reply to Theme</h2>
    <div class="reply-form">
      <label for="replyContent">Your Reply:</label>
      <textarea id="replyContent" name="replyContent"></textarea><br><br>
      <button id="submitReplyButton">Send Reply</button>
    </div>
  `;

  widget.node.innerHTML = replyFormHTML; // Update widget's HTML

  // Event listener for "Send Reply" button
  const submitReplyButton = widget.node.querySelector('#submitReplyButton');
  if (submitReplyButton) {
    submitReplyButton.addEventListener('click', async () => {
      const replyContentInput = widget.node.querySelector('#replyContent') as HTMLTextAreaElement;

      const newReply = {
        Content: replyContentInput.value,
        Author: username,
        ThemeID: themeId,
        // Add other relevant fields if necessary
      };

      try {
        // Send reply data to the server
        const response = await fetch(forumEndpointUrl + "replytheme", {
          method: 'POST',
          body: JSON.stringify(newReply),
          headers: { 'Content-Type': 'application/json' },
        });

        if (response.ok) {
          // Reply sent successfully
          const data = await response.json();
          const replyId = data.ReplyID;

          ShowThemeDetail(widget, themeId, forumEndpointUrl, username); // Show the details of the new theme
          // Optionally, display a confirmation message or update the UI
          console.log('Reply sent successfully with ID:', replyId);
          // You can call another function to update the UI with the new reply
        } else {
          // Handle errors here
          console.error('Failed to send reply:', response.status);
          ShowThemeDetail(widget, themeId, forumEndpointUrl, username); // Show the details of the new theme
        }
      } catch (error) {
        console.error('Error sending reply:', error);
        // Handle errors here
      }
    });
  }
}
