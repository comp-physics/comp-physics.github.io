module Jekyll
  # Liquid filters for cleaning up rendered BibTeX before it is shown/copied.
  module BibtexFilters
    # Remove internal-only fields from a rendered BibTeX string.
    #
    # The `file` field points at the in-repo PDF for the publications-page PDF
    # button; it is meaningless to anyone copying the citation, so strip it (and
    # any other fields passed as a comma-separated list) from the displayed BibTeX.
    #
    #   {{ entry.bibtex | strip_bibtex_fields }}            # strips `file`
    #   {{ entry.bibtex | strip_bibtex_fields: "file,note" }}
    def strip_bibtex_fields(input, fields = "file")
      return input if input.nil?

      names = fields.to_s.split(",").map { |f| Regexp.escape(f.strip) }.reject(&:empty?)
      return input if names.empty?

      # Match a whole field line: `  file = {value},` (optional trailing comma).
      pattern = /^[ \t]*(?:#{names.join('|')})[ \t]*=[ \t]*\{[^}]*\},?[ \t]*\r?\n/i
      input.gsub(pattern, "")
    end
  end
end

Liquid::Template.register_filter(Jekyll::BibtexFilters)
