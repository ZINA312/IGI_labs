let currentPage = 1;
const itemsPerPage = 3;
let contacts = [];
let ascending = true;
let currentColumnIndex = 0;

document.getElementById('addButton').onclick = function() {
    document.getElementById('contactForm').classList.toggle('hidden');
};

document.getElementById('submitContact').onclick = function() {
    const name = document.getElementById('name').value.trim();
    const photoUrl = document.getElementById('photoUrl').value.trim();
    const description = document.getElementById('description').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const email = document.getElementById('email').value.trim();

    const urlValid = validateUrl(photoUrl);
    const phoneValid = validatePhone(phone);
    const validationMessage = document.getElementById('validationMessage');

    document.getElementById('photoUrl').classList.remove('highlight');
    document.getElementById('phone').classList.remove('highlight');

    if (urlValid && phoneValid) {
        validationMessage.innerText = '';
        contacts.push({ name, photoUrl, description, phone, email });
        console.log(contacts);
        
        document.getElementById('contactForm').classList.add('hidden'); 
        clearForm();
        renderTable(); 
        updatePagination();
    } else {
        validationMessage.innerText = 'Пожалуйста, исправьте ошибки в форме.';
        if (!urlValid) {
            document.getElementById('photoUrl').classList.add('highlight');
        }
        if (!phoneValid) {
            document.getElementById('phone').classList.add('highlight');
        }
    }
};

function clearForm() {
    document.getElementById('name').value = '';
    document.getElementById('photoUrl').value = '';
    document.getElementById('description').value = '';
    document.getElementById('phone').value = '';
    document.getElementById('email').value = '';
}

function showLoader() {
    document.getElementById('loader').style.display = 'block';
}

function hideLoader() {
    document.getElementById('loader').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    loadTable();
});

function loadTable() {
    showLoader();
    fetch('/api/contacts')
    .then(response => response.json())
    .then(data => {
        contacts = data;
        renderTable(); 
        updatePagination();
    })
    .catch(error => console.error('Ошибка:', error))
    .finally(() => {
        hideLoader(); 
    });
}

function renderTable() {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = Math.min(startIndex + itemsPerPage, contacts.length);
    console.log(contacts);
    for (let i = startIndex; i < endIndex; i++) {
        const contact = contacts[i];
        const row = `<tr onclick="showDetails(${i})">
            <td>${contact.name}</td>
            <td><img src="${contact.photo}" alt="${contact.name}" style="width: 50px;"></td>
            <td>${contact.description}</td>
            <td>${contact.phone}</td>
            <td>${contact.email}</td>
            <td><input type="checkbox" class="contactCheckbox" data-name="${contact.name}"></td>
        </tr>`;
        tableBody.innerHTML += row;
    }
}

function showDetails(index) {
    const detailsBlock = document.getElementById('detailsBlock');
    const contact = contacts[index];
    detailsBlock.innerHTML = `
        <h3>Детали контакта:</h3>
        <p>ФИО: ${contact.name}</p>
        <p>Описание: ${contact.description}</p>
        <p>Телефон: ${contact.phone}</p>
        <p>Email: ${contact.email}</p>
    `;
    detailsBlock.classList.remove('hidden');
}

function sortTable(columnIndex) {
    ascending = !ascending;
    const keys = ["name", "photoUrl", "description", "phone", "email"];
    
    contacts.sort((a, b) => {
        let aValue = a[keys[columnIndex]];
        let bValue = b[keys[columnIndex]];

        if (typeof aValue === 'string') {
            aValue = aValue.toLowerCase();
            bValue = bValue.toLowerCase();
        }

        return ascending ? (aValue > bValue ? 1 : -1) : (aValue < bValue ? 1 : -1);
    });

    const indicators = document.querySelectorAll('.sort-indicator');
    indicators.forEach(indicator => indicator.innerText = '');

    const sortIndicator = document.getElementById(`sortIndicator${columnIndex}`);
    if (sortIndicator) {
        sortIndicator.innerText = ascending ? '↑' : '↓';
    }

    renderTable(); 
}

function validateUrl(url) {
    const regex = /^(https?:\/\/).+\.(php|html)$/;
    return regex.test(url);
}

function validatePhone(phone) {
    const regex = /^(8\d{10}|\+375\s?\(29\)\s?\d{3}[-]?\s?\d{2}[-]?\s?\d{2}|\+375\s?29\s?\d{3}[-]?\s?\d{2}[-]?\s?\d{2}|8\s?\(029\)\s?\d{7})$/;
    return regex.test(phone);
}

document.getElementById('filterBtn').onclick = function() {
    const filterValue = document.getElementById('filter').value.toLowerCase();
    if (filterValue === '') {
        loadTable();
        return;
    }
    const filteredContacts = contacts.filter(contact => contact.name.toLowerCase().includes(filterValue));
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';
    filteredContacts.forEach(contact => {
        const index = contacts.indexOf(contact);
        const row = `<tr onclick="showDetails(${index})">
            <td>${contact.name}</td>
            <td><img src="${contact.photoUrl}" alt="${contact.name}" style="width: 50px;"></td>
            <td>${contact.description}</td>
            <td>${contact.phone}</td>
            <td>${contact.email}</td>
            <td><input type="checkbox" class="contactCheckbox" data-name="${contact.name}"></td>
        </tr>`;
        tableBody.innerHTML += row;
    });
};

document.getElementById('rewardBtn').onclick = function() {
    const checkboxes = document.querySelectorAll('.contactCheckbox:checked');
    const names = Array.from(checkboxes).map(cb => cb.dataset.name);
    const rewardMessage = document.getElementById('rewardMessage');
    if (names.length > 0) {
        rewardMessage.innerText = `Премируемые: ${names.join(', ')}`;
    } else {
        rewardMessage.innerText = 'Не выбраны сотрудники для премирования.';
    }
};

function updatePagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';

    const totalPages = Math.ceil(contacts.length / itemsPerPage);
    for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.innerText = i;
        pageButton.onclick = function() {
            currentPage = i;
            renderTable(); 
        };
        pagination.appendChild(pageButton);
    }
}