/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ListRenderer } from '@web/views/list/list_renderer';
import { useEffect } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";


const CellLimitThreshold = 100; // px (height to trigger the limit cell feature)

// see static/src/css/list_renderer.css
const LimitCellClass = 'o_limit_cell';
const LimitCellArrowClass = 'o_limit_cell_arrow';


patch(ListRenderer.prototype, 'list_renderer_limit_cell', {
    setup() {
        this._super(...arguments);

        this.limit_fields = this.props.list.context?.limit_fields;
        useEffect(() => {
            if (this.limit_fields) {
                this.limitCellsHeight();
            }
        });
    },

    limitCellsHeight() {
        this.tableRef.el.querySelectorAll('td.o_data_cell').forEach((cellEl) => {
            if (this.limit_fields.includes(cellEl.getAttribute('name'))
                && cellEl.offsetHeight > CellLimitThreshold // too tall
            ) {
                // Wrap the content of the cell in a div
                let div = document.createElement('div');
                div.classList.add(LimitCellClass);
                div.innerHTML = cellEl.innerHTML;
                cellEl.innerHTML = '';
                cellEl.appendChild(div);

                // Add a arrow down to expand the cell
                let downArrow = document.createElement('i');
                downArrow.classList.add('fa', 'fa-angle-down', LimitCellArrowClass);
                downArrow.addEventListener('click',  this.onArrowClick.bind(this));
                cellEl.appendChild(downArrow);

                // Add a arrow up to collapse the cell
                let upArrow = document.createElement('i');
                upArrow.classList.add('fa', 'fa-angle-up', LimitCellArrowClass, 'd-none');
                upArrow.addEventListener('click', this.onArrowClick.bind(this));
                cellEl.appendChild(upArrow);
            }
        });
    },

    onArrowClick(event) {
        event.stopPropagation();

        let cell = event.target.parentElement;

        cell.querySelector('div').classList.toggle(LimitCellClass)
        cell.querySelectorAll(`.${LimitCellArrowClass}`).forEach((arrow) => {
            arrow.classList.toggle('d-none');
        });
    }
});

export default ListRenderer;
