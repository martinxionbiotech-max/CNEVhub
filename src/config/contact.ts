/**
 * Contact Page Configuration — EV Hub
 *
 * Real company + author contact information for EEAT.
 * Company: Chengguang Energy (Jinzhou Chengguang Power Source Co., Ltd.)
 * Author: Wei Wang, EV & Battery Industry Analyst
 * Primary contact: Martin
 */

import type { ContactInfo, ContactMethod, ContactFAQ } from '../lib/types';

/** Contact information used across contact page and legal pages */
export const contact: ContactInfo = {
  email: 'martin@dinweys.com',
  supportEmail: 'martin@dinweys.com',
  salesEmail: 'martin@dinweys.com',
  address: {
    street: 'Jinzhou, Hebei',
    city: 'Jinzhou',
    state: 'Hebei',
    zip: '',
    country: 'China',
  },
};

/** Contact methods displayed on the contact page */
export const contactMethods: ContactMethod[] = [
  {
    icon: 'lucide:mail',
    label: 'Email',
    value: 'martin@dinweys.com',
    href: 'mailto:martin@dinweys.com',
  },
  {
    icon: 'lucide:message-circle',
    label: 'WhatsApp / WeChat',
    value: '+86 13323237275',
    href: 'https://wa.me/8613323237275',
  },
  {
    icon: 'lucide:phone',
    label: 'Phone',
    value: '+86 13323237275',
    href: 'tel:+8613323237275',
  },
];

/** FAQ items displayed on the contact page */
export const contactFAQs: ContactFAQ[] = [
  {
    question: "What's your typical response time?",
    answer: 'We respond to most inquiries within 24 hours on business days (GMT+8).',
  },
  {
    question: 'Can you help me source a specific Chinese EV?',
    answer:
      'Yes. Send us the model and destination country, and we will provide a transparent landed-cost breakdown including duties, countervailing tariffs, VAT, freight, and certification.',
  },
  {
    question: 'Do you sell vehicles directly?',
    answer:
      'No. EV Hub is an independent information platform. We provide landed-cost intelligence and sourcing guidance, but do not sell vehicles or act on behalf of any manufacturer.',
  },
];

