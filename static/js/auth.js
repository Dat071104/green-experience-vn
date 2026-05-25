document.addEventListener('DOMContentLoaded', () => {
    // 1. Password toggle
    const toggleBtns = document.querySelectorAll('.password-toggle');
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.previousElementSibling;
            const icon = this.querySelector('i');
            
            if (input.type === 'password') {
                input.type = 'text';
                icon.setAttribute('data-lucide', 'eye-off');
            } else {
                input.type = 'password';
                icon.setAttribute('data-lucide', 'eye');
            }
            lucide.createIcons();
        });
    });

    // 2. Role selection
    const roleTabs = document.querySelectorAll('.role-tab');
    const roleInput = document.getElementById('role-input');
    const staffCodeGroup = document.getElementById('staff-code-group');
    const staffCodeInput = document.getElementById('staff-code');
    
    if (roleTabs.length > 0 && roleInput) {
        roleTabs.forEach(tab => {
            tab.addEventListener('click', function() {
                // Remove active from all
                roleTabs.forEach(t => t.classList.remove('active'));
                // Add active to clicked
                this.classList.add('active');
                
                // Update hidden input
                const selectedRole = this.getAttribute('data-role');
                roleInput.value = selectedRole;
                
                // Show/hide staff code input
                if (staffCodeGroup) {
                    if (selectedRole === 'staff') {
                        staffCodeGroup.style.display = 'block';
                        staffCodeInput.setAttribute('required', 'required');
                    } else {
                        staffCodeGroup.style.display = 'none';
                        staffCodeInput.removeAttribute('required');
                    }
                }
            });
        });
    }
});
