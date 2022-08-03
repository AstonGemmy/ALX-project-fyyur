// Delete venue
document.querySelectorAll('.delete-venue').forEach(deleteButton => {
  deleteButton.addEventListener('click', (e) => {
    const venueId = e.target.dataset.id;
    fetch('/venues/' + venueId, {
      method: 'DELETE'
    })
    .then(response => response.json())
    .then(response => {
      if (response.status) window.location = response.next;
    })
    .catch((e) => {
      console.log('Error occurred while attempting to delete venue record.')
    })
  })
})

// Append availability times to "Start Time" input section when artist id is entered
// This guides venue owners on what time to schedule shows for artists with
// availability times
document.querySelector('#show-artist-id').addEventListener('keyup', (e) => {
  const artistId = e.target.value;
  if (artistId) {
    fetch('/artists/availability/' + artistId, {
      method: 'POST'
    })
    .then(response => response.json())
    .then(response => {
      if (response.status && response.availability.length) {
        const isPlural = () => response.availability.length > 1
        document.querySelector('#availability').innerHTML = `
          Selected artist's availability time${isPlural() ? 's' : ''} 
          ${isPlural() ? 'are' : 'is'} ${response.availability.join(', ')}
        `
      } else {
        document.querySelector('#availability').innerHTML = ''
      }
    })
    .catch((e) => {
      console.log('Error occurred while fetching artist availability.')
    })
  } else {
    document.querySelector('#availability').innerHTML = ''
  }
})