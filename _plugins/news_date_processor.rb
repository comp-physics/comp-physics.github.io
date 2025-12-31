module Jekyll
  class NewsDateProcessor < Generator
    safe true
    priority :low

    def generate(site)
      return unless site.data['news']
      
      site.data['news'].each do |item|
        # Only process if date_iso doesn't exist
        next if item['date_iso']
        next unless item['date']
        
        begin
          # Parse the date string (handles formats like "December 22, 2025", "22 December 2025", etc.)
          parsed_date = Date.parse(item['date'])
          
          # Set date_iso in ISO format (YYYY-MM-DD)
          item['date_iso'] = parsed_date.strftime('%Y-%m-%d')
          
          # Set display_date to original date if not already set
          item['display_date'] ||= item['date']
        rescue ArgumentError
          # If date parsing fails, skip this item
          Jekyll.logger.warn "News Date Processor:", "Could not parse date: #{item['date']}"
        end
      end
    end
  end
end

