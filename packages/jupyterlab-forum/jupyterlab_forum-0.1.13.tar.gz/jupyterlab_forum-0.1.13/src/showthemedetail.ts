import{handleReplyToTheme} from './replytheme';
import{fetchGroupData} from './getgroupinfo';

export async function ShowThemeDetail(widget: any, ThemeID: any, forumEndpointUrl: string, username: string) {

    // Example theme data
    const exampleTheme = {
      Title: "Example Theme",
      Description: "This is an example theme description.",
      Author: "User123",
      CreationTime: "2024-07-24T10:08",
      Status: "Open",
      Replies: [
        { Author: "Example Author2", Content: "This is an example reply to the theme2.", CreationTime: "2024-07-22T10:08" },
        { Author: "Example Author", Content: "This is an example reply to the theme.", CreationTime: "2024-07-24T10:08" },
      ]
    };

    try {

        const grouplist = await fetchGroupData( forumEndpointUrl)
        // Make a POST request to retrieve the theme details
        const response = await fetch(forumEndpointUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ThemeID: ThemeID }),
        });

        const themeDetail = await response.json();
        // Update the widget's HTML to display the theme details
        widget.node.innerHTML = `
          <div class="topic">
            <div class="topic-header">
              <h2 class="topic-title">${themeDetail.Title}</h2>
              <div class="topic-meta">
                <span class="topic-author">by ${themeDetail.Author}</span>
                <span class="topic-date">${new Date(themeDetail.CreationTime).toLocaleDateString()}</span>
              </div>
            </div>

            <div class="topic-body">
              <div class="topic-content">${themeDetail.Description}</div>
              <div class="topic-stats">
                <span>${themeDetail.Replies.length} Antworten</span> •
              </div>
            </div>

            <div class="topic-replies">
              <h3>Antworten</h3>
              <div class="replies-container">  </div>
            </div>

            <button id="reply-to-theme" class="btn btn-primary">Reply</button>
            <button id="back-to-forum" class="btn btn-primary">Back to Forum</button>
            ${(username === themeDetail.Author || grouplist.includes(username)) ? `
              <button id="delete-theme" class="btn btn-danger">Delete Theme</button>
              ${(username === themeDetail.Author || grouplist.includes(username)) ? `
                <button id="toggle-status" class="btn btn-secondary">${themeDetail.Status === 'Open' ? 'Close' : 'Open'} Theme</button>
              ` : ''}
            ` : ''}
          </div>
        `;

        // Insert replies into replies-container
        const repliesContainer = widget.node.querySelector('.replies-container');
        themeDetail.Replies.forEach((reply: any) => {
            const replyDiv = document.createElement('div');
            replyDiv.className = 'reply';
            replyDiv.innerHTML = `
              <div class="reply-header">
                <span class="reply-author">${reply.Author}</span> •
                <span class="reply-date">${new Date(reply.CreationTime).toLocaleDateString()}</span>
              </div>
              <div class="reply-content">${reply.Content}</div>
            `;
            repliesContainer?.appendChild(replyDiv); // Add the reply div to the container
          });

          // Event listener for toggle status button
          const toggleStatusButton = widget.node.querySelector('#toggle-status');
          if (toggleStatusButton) {
              toggleStatusButton.addEventListener('click', async () => {
                  try {
                      const newStatus = themeDetail.Status === 'Open' ? 'Closed' : 'Open';
                      const response = await fetch(`${forumEndpointUrl}/togglestatus`, {
                          method: 'PATCH',
                          headers: {
                              'Content-Type': 'application/json',
                          },
                          body: JSON.stringify({ ThemeID: ThemeID, Status: newStatus }),
                      });

                      if (response.ok) {
                          ShowThemeDetail(widget, ThemeID, forumEndpointUrl, username); // Refresh the theme detail
                      } else {
                          console.error('Failed to toggle status:', response.status);
                      }
                  } catch (error) {
                      console.error('Error toggling status:', error);
                  }
              });
          }


    } catch (error) {
        console.error('Error fetching theme details:', error);

        const themeDetail = exampleTheme;
        // Update the widget's HTML to display the theme details
        widget.node.innerHTML = `
          <div class="topic">
            <div class="topic-header">
              <h2 class="topic-title">${themeDetail.Title}</h2>
              <div class="topic-meta">
                <span class="topic-author">by ${themeDetail.Author}</span>
                <span class="topic-date">${new Date(themeDetail.CreationTime).toLocaleDateString()}</span>
              </div>
            </div>

            <div class="topic-body">
              <div class="topic-content">${themeDetail.Description}</div>
              <div class="topic-stats">
                <span>${themeDetail.Replies.length} Antworten</span> •
              </div>
            </div>

            <div class="topic-replies">
              <h3>Antworten</h3>
              <div class="replies-container">  </div>
            </div>

            <button id="reply-to-theme" class="btn btn-primary">Reply</button>
            <button id="back-to-forum" class="btn btn-primary">Back to Forum</button>

            <button id="delete-theme" class="btn btn-danger">Delete Theme</button>

            <button id="toggle-status" class="btn btn-secondary">${themeDetail.Status === 'Open' ? 'Close' : 'Open'} Theme</button>

          </div>
        `;

        // Insert replies into replies-container
        const repliesContainer = widget.node.querySelector('.replies-container');
        themeDetail.Replies.forEach((reply: any) => {
            const replyDiv = document.createElement('div');
            replyDiv.className = 'reply';
            replyDiv.innerHTML = `
              <div class="reply-header">
                <span class="reply-author">${reply.Author}</span> •
                <span class="reply-date">${new Date(reply.CreationTime).toLocaleDateString()}</span>
              </div>
              <div class="reply-content">${reply.Content}</div>
            `;
            repliesContainer?.appendChild(replyDiv); // Add the reply div to the container
          });

        // Event listener for toggle status button
        const toggleStatusButton = widget.node.querySelector('#toggle-status');
        if (toggleStatusButton) {
            toggleStatusButton.addEventListener('click', async () => {
                try {
                    const newStatus = themeDetail.Status === 'Open' ? 'Closed' : 'Open';
                    const response = await fetch(`${forumEndpointUrl}/togglestatus`, {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ ThemeID: ThemeID, Status: newStatus }),
                    });

                    if (response.ok) {
                        ShowThemeDetail(widget, ThemeID, forumEndpointUrl, username); // Refresh the theme detail
                    } else {
                        console.error('Failed to toggle status:', response.status);
                    }
                } catch (error) {
                    console.error('Error toggling status:', error);
                }
            });
        }

      }

    const backButton = widget.node.querySelector('#back-to-forum');
    backButton?.addEventListener('click', () => {
        widget.node.innerHTML = widget.originalHTML;
        widget.fetchAndDisplayThemes();
    });

    // Event listener for reply button
    const replyButton = widget.node.querySelector('#reply-to-theme');
    replyButton?.addEventListener('click', () => {
        handleReplyToTheme(widget, username, ThemeID, forumEndpointUrl);
    });


    // Event listener for delete button
    const deleteButton = widget.node.querySelector('#delete-theme');
    if (deleteButton) {
        deleteButton.addEventListener('click', async () => {
            try {
                const response = await fetch(`${forumEndpointUrl}/deletetheme`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ThemeID: ThemeID }),
                });

                if (response.ok) {
                    widget.node.innerHTML = widget.originalHTML;
                    widget.fetchAndDisplayThemes();
                } else {
                    console.error('Failed to delete theme:', response.status);
                }
            } catch (error) {
                console.error('Error deleting theme:', error);
            }
        });
    }

}
