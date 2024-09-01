document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.getElementById('search-bar');
    const resultsContainer = document.getElementById('results');

    searchBar.addEventListener('input', function() {
        const query = searchBar.value.trim();

        if (query.length > 0) {
            fetch(`/search?query=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    resultsContainer.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(item => {
                            const resultItem = document.createElement('div');
                            resultItem.classList.add('result-item');
                            resultItem.innerHTML = `<h3>${item.title || item.name}</h3><p>${item.content || 'No content available'}</p>`;
                            resultsContainer.appendChild(resultItem);
                        });
                    } else {
                        resultsContainer.innerHTML = '<p>No results found.</p>';
                    }
                })
                .catch(error => {
                    console.error('Error fetching search results:', error);
                });
        } else {
            resultsContainer.innerHTML = '';
        }
    });
});
