from django.contrib import admin
from django.utils.html import format_html
from .models import CallbackRequest

@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    # Professional display with quick actions
    list_display = (
        "name_with_status",
        "contact_info",
        "service_badge",
        "created_at_formatted",
        "quick_actions",
    )

    list_filter = ("service", "created_at")  # Sidebar filters
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)
    list_per_page = 20

    # 1️⃣ Premium Name Display with online dot
    def name_with_status(self, obj):
        return format_html(
            '<div style="display: flex; align-items: center;">'
            '<div style="width: 8px; height: 8px; border-radius: 50%; background: #10b981; margin-right: 10px;"></div>'
            '<div>'
            '<strong style="font-size: 14px; color: #1e293b;">{}</strong><br>'
            '<small style="color: #64748b;">ID: #{}</small>'
            '</div>'
            '</div>',
            obj.name,
            obj.id
        )
    name_with_status.short_description = "Client Name"

    # 2️⃣ Contact Info
    def contact_info(self, obj):
        return format_html(
            '<div style="line-height: 1.6;">'
            '<span style="color: #3b82f6; font-weight: 500;">✉ {}</span><br>'
            '<span style="color: #64748b;">✆ {}</span>'
            '</div>',
            obj.email,
            obj.phone
        )
    contact_info.short_description = "Contact Details"

    # 3️⃣ Service Badge
    def service_badge(self, obj):
        colors = {
            "Accounting": ("#dcfce7", "#166534"),       # Green
            "Taxation": ("#ffedd5", "#9a3412"),         # Orange
            "General Inquiry": ("#f1f5f9", "#475569"),  # Gray
        }
        bg, text = colors.get(obj.service, ("#dbeafe", "#1e40af")) # Default Blue
        return format_html(
            '<span style="background: {}; color: {}; padding: 4px 12px; '
            'border-radius: 9999px; font-size: 11px; font-weight: 700; '
            'text-transform: uppercase; letter-spacing: 0.025em; border: 1px solid rgba(0,0,0,0.1);">'
            '{}'
            '</span>',
            bg, text, obj.service
        )
    service_badge.short_description = "Service Category"

    # 4️⃣ Formatted created_at
    def created_at_formatted(self, obj):
        return format_html(
            '<span style="color: #64748b; font-size: 13px;">{}</span>',
            obj.created_at.strftime("%b %d, %Y | %H:%M")
        )
    created_at_formatted.short_description = "Requested On"

    # 5️⃣ Quick action buttons
    def quick_actions(self, obj):
        return format_html(
            '<div style="display: flex; gap: 8px;">'
            '<a href="tel:{}" title="Call Client" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 4px; color: #64748b;">📞</a>'
            '<a href="mailto:{}" title="Email Client" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 4px; color: #64748b;">✉</a>'
            '</div>',
            obj.phone,
            obj.email
        )
    quick_actions.short_description = "Actions"

    # 6️⃣ Optional: Add custom CSS/JS
    class Media:
        css = {
            'all': ('css/admin_custom.css',)  # Create this file in static for custom styling
        }
        js = ('js/admin_custom.js',)  # Optional JS for extra interactivity