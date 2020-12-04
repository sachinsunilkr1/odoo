odoo.define('pos_order_history.Button', function (require) {
"use strict";

var core = require('web.core');
var pos_screens = require('point_of_sale.screens');
var models = require('point_of_sale.models');
var field_utils = require('web.field_utils');
var gui = require('point_of_sale.gui');
var chrome = require('point_of_sale.chrome');
var _t = core._t;
var QWeb = core.qweb;
var PosModelSuper = models.PosModel;
// On button click redirect to next order history screen
var ShowOrderButton = pos_screens.ActionButtonWidget.extend({
    template: 'ShowOrderButton',
//    console.log(widget.pos.get_client().id)
    button_click: function(){
         this.gui.show_screen('ShowOrdersWidget')

    }
});
pos_screens.define_action_button({
    'name': 'Show Order',
    'widget': ShowOrderButton,
    'condition': function(){
        return this.pos;
    },
});

});
