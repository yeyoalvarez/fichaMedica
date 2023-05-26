
jQuery(function ($) {
  var linkStyle =
    'cursor: pointer; color: #fff; border-radius: 4px; font-weight: 400; padding: 5px 10px; background: #417690; border: none;';

  // Only for stacked inlines
  $('div.inline-group div.inline-related:not(.tabular)').each(function () {
    const $h3 = $(this.querySelector('h3'));
    const $fs = $(this.querySelector('fieldset'));
    const fsErrorsExist = $fs.children('.errors').length;
    const initialButtonText = fsErrorsExist ? gettext('Hide') : gettext('Show');
    const $button = $(
      $.parseHTML(
        '<a role="button" style="' +
          linkStyle +
          '" class="stacked_collapse-toggle">' +
          initialButtonText +
          '</a> '
      )
    );

    // Don't collapse initially if fieldset contains errors
    if (fsErrorsExist) $fs.addClass('stacked_collapse');
    else $fs.addClass('stacked_collapse collapsed');

    $h3.prepend($button);
  });

  // Hide/Show button click
  $('div.inline-group').on('click', '.stacked_collapse-toggle', function () {
    const $fs = $(this).parents('.inline-related').children('fieldset')
    if (!$fs.hasClass('collapsed')) {
      $fs.addClass('collapsed');
      this.innerHTML = gettext('Show');
    } else {
      $fs.removeClass('collapsed');
      this.innerHTML = gettext('Hide');
    }
  })
});