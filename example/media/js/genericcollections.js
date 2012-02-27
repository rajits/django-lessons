function showGenericRelatedObjectLookupPopup(triggeringLink, ctArray) {
    var realName = triggeringLink.id.replace(/^lookup_/, '');
    var name = id_to_windowname(realName);
    realName = realName.replace(/object_id/, 'content_type');
    var select = document.getElementById(realName);
    if (select.selectedIndex === 0) {
        alert("Select a content type first.");
        return false;
    }
    var selectedItem = select.item(select.selectedIndex).value;
    return showRelatedObjectLookupPopup(name, triggeringLink, ctArray[selectedItem]);
}

function showGenericRequiredModelLookupPopup(triggeringLink, ctItem) {
    ctItem = ctItem.replace('.', '/');
    var realName = triggeringLink.id.replace(/^lookup_/, '');
    var name = id_to_windowname(realName);
    return showRelatedObjectLookupPopup(name, triggeringLink, ctItem);
}

function showRelatedObjectLookupPopup(name, triggeringLink, ctItem) {
    var href = triggeringLink.href.replace(/#/,'../../../' + ctItem + '/?t=id');
    if (href.search(/\?/) >= 0) {
        href = href + '&pop=1';
    } else {
        href = href + '?pop=1';
    }
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}
